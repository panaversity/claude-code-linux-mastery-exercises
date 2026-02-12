#!/usr/bin/env node
/**
 * Support Agent - AI-powered customer support chat agent.
 *
 * Handles incoming chat messages, routes them through an LLM with
 * RAG-enhanced context from the knowledge base, and returns responses.
 *
 * Listens on port 8002.
 */

const express = require("express");
const cors = require("cors");
const { OpenAI } = require("openai");
const fs = require("fs");
const path = require("path");

const CONFIG_PATH =
  process.env.CONFIG_PATH || "/etc/support-agent/config.json";

// Load configuration
const config = JSON.parse(fs.readFileSync(CONFIG_PATH, "utf8"));

const app = express();
app.use(express.json());
app.use(cors({ origin: config.server.cors_origins }));

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Session store (in-memory fallback)
const sessions = new Map();

// Health check
app.get("/health", (req, res) => {
  res.json({
    status: "healthy",
    service: "support-agent",
    model: config.llm.model,
    uptime: process.uptime(),
  });
});

// Chat endpoint
app.post("/chat", async (req, res) => {
  const { session_id, message } = req.body;

  if (!message) {
    return res.status(400).json({ error: "Message is required" });
  }

  try {
    // Get or create session
    let history = sessions.get(session_id) || [];

    // Add user message
    history.push({ role: "user", content: message });

    // Call LLM
    const completion = await openai.chat.completions.create({
      model: config.llm.model,
      messages: [
        {
          role: "system",
          content:
            "You are a helpful customer support agent. Be concise and friendly.",
        },
        ...history.slice(-10), // Last 10 messages for context
      ],
      max_tokens: config.llm.max_tokens,
      temperature: config.llm.temperature,
    });

    const reply = completion.choices[0].message.content;

    // Save to session
    history.push({ role: "assistant", content: reply });
    sessions.set(session_id, history);

    console.log(
      `[${new Date().toISOString()}] session=${session_id} tokens=${completion.usage.total_tokens}`
    );

    res.json({
      reply,
      session_id,
      tokens_used: completion.usage.total_tokens,
    });
  } catch (err) {
    console.error(`[${new Date().toISOString()}] ERROR: ${err.message}`);
    res.status(500).json({ error: "Internal server error" });
  }
});

// List active sessions (admin)
app.get("/admin/sessions", (req, res) => {
  res.json({
    active_sessions: sessions.size,
    session_ids: Array.from(sessions.keys()),
  });
});

// Start server
const PORT = config.server.port || 8002;
app.listen(PORT, config.server.host, () => {
  console.log(`[${new Date().toISOString()}] Support Agent listening on port ${PORT}`);
  console.log(`[${new Date().toISOString()}] Model: ${config.llm.model}`);
  console.log(`[${new Date().toISOString()}] Knowledge base: ${config.knowledge_base.path}`);
});
