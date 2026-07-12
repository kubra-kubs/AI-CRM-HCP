import { Box, Typography } from "@mui/material";
import { useState } from "react";

import LeftPanel from "../components/LeftPanel";
import RightPanel from "../components/RightPanel";

export default function Dashboard() {

  const [interactionData, setInteractionData] = useState({
    hcp_name: "",
    interaction_type: "",
    date: "",
    time: "",
    attendees: "",
    topics: "",
    materials: "",
    samples: "",
    sentiment: "",
    outcomes: "",
    followup: "",
  });

  return (
    <Box
      sx={{
        minHeight: "100vh",
        background: "#f5f7fb",
        p: 3,
      }}
    >
      <Typography
        variant="h4"
        fontWeight="bold"
        sx={{ mb: 3 }}
      >
        AI CRM - HCP Module
      </Typography>

      <Box
        sx={{
          display: "flex",
          gap: 3,
        }}
      >
        <LeftPanel
          interactionData={interactionData}
        />

        <RightPanel
          setInteractionData={setInteractionData}
        />
      </Box>
    </Box>
  );
}