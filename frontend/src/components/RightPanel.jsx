import { useState } from "react";

import {
  Paper,
  Typography,
  Box,
  TextField,
  IconButton,
} from "@mui/material";

import SendIcon from "@mui/icons-material/Send";

import api from "../services/api";

export default function RightPanel({ setInteractionData }) {

  const [message, setMessage] = useState("");

  const [chat, setChat] = useState([
    {
      sender: "AI",
      text: "👋 Hello! Describe your interaction with the HCP."
    }
  ]);

  const sendMessage = async () => {

    if (!message.trim()) return;

    const userMessage = message;

    setChat((prev) => [
      ...prev,
      {
        sender: "You",
        text: userMessage,
      },
    ]);

    setMessage("");

    try {

      const res = await api.post("/chat", {
        message: userMessage,
      });

      setInteractionData(res.data);

      setChat((prev) => [
        ...prev,
        {
          sender: "AI",
          text: "✅ Interaction extracted successfully.",
        },
      ]);

    } catch (err) {

      console.error(err);

      setChat((prev) => [
        ...prev,
        {
          sender: "AI",
          text: "❌ Failed to process interaction.",
        },
      ]);

    }

  };

  return (
    <Paper
      elevation={3}
      sx={{
        flex: 1,
        p: 3,
        borderRadius: 3,
        display: "flex",
        flexDirection: "column",
        height: "85vh",
      }}
    >

      <Typography
        variant="h6"
        fontWeight="bold"
        mb={2}
      >
        AI Assistant
      </Typography>

      <Box
        sx={{
          flex: 1,
          background: "#f5f5f5",
          borderRadius: 2,
          p: 2,
          overflowY: "auto",
          mb: 2,
        }}
      >

        {chat.map((msg, index) => (

          <Box
            key={index}
            sx={{
              mb: 2,
            }}
          >

            <Typography
              fontWeight="bold"
            >
              {msg.sender}
            </Typography>

            <Typography
              sx={{
                background: "white",
                p: 1.5,
                borderRadius: 2,
                width: "fit-content",
              }}
            >
              {msg.text}
            </Typography>

          </Box>

        ))}

      </Box>

      <Box
        sx={{
          display: "flex",
          gap: 1,
        }}
      >

        <TextField
          fullWidth
          value={message}
          placeholder="Describe your interaction..."
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <IconButton
          onClick={sendMessage}
          color="primary"
          sx={{
            bgcolor: "#1976d2",
            color: "white",
            "&:hover": {
              bgcolor: "#1565c0",
            },
          }}
        >
          <SendIcon />
        </IconButton>

      </Box>

    </Paper>
  );
}