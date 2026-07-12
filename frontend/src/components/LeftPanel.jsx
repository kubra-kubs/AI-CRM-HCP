import {
  Paper,
  Typography,
  TextField,
  MenuItem,
  Box,
  Button,
} from "@mui/material";

export default function LeftPanel({ interactionData }) {
  return (
    <Paper
      elevation={3}
      sx={{
        flex: 1,
        p: 3,
        borderRadius: 3,
      }}
    >
      <Typography variant="h6" fontWeight="bold" mb={3}>
        Interaction Details
      </Typography>

      <TextField
        label="HCP Name"
        fullWidth
        margin="normal"
        value={interactionData.hcp_name}
        InputProps={{ readOnly: true }}
      />

      <TextField
        label="Interaction Type"
        fullWidth
        margin="normal"
        select
        value={interactionData.interaction_type}
        InputProps={{ readOnly: true }}
      >
        <MenuItem value="Meeting">Meeting</MenuItem>
        <MenuItem value="Call">Call</MenuItem>
        <MenuItem value="Email">Email</MenuItem>
      </TextField>

      <Box sx={{ display: "flex", gap: 2 }}>
        <TextField
          label="Date"
          fullWidth
          margin="normal"
          value={interactionData.date}
          InputProps={{ readOnly: true }}
        />

        <TextField
          label="Time"
          fullWidth
          margin="normal"
          value={interactionData.time}
          InputProps={{ readOnly: true }}
        />
      </Box>

      <TextField
        label="Attendees"
        fullWidth
        margin="normal"
        value={interactionData.attendees}
        InputProps={{ readOnly: true }}
      />

      <TextField
        label="Topics Discussed"
        multiline
        rows={3}
        fullWidth
        margin="normal"
        value={interactionData.topics}
        InputProps={{ readOnly: true }}
      />

      <Button
        variant="outlined"
        fullWidth
        sx={{ mt: 2, mb: 2 }}
      >
        🎤 Summarize from Voice Note
      </Button>

      <TextField
        label="Materials Shared"
        fullWidth
        margin="normal"
        value={interactionData.materials}
        InputProps={{ readOnly: true }}
      />

      <TextField
        label="Samples Distributed"
        fullWidth
        margin="normal"
        value={interactionData.samples}
        InputProps={{ readOnly: true }}
      />

      <TextField
        label="HCP Sentiment"
        fullWidth
        margin="normal"
        value={interactionData.sentiment}
        InputProps={{ readOnly: true }}
      />

      <TextField
        label="Outcomes"
        multiline
        rows={2}
        fullWidth
        margin="normal"
        value={interactionData.outcomes}
        InputProps={{ readOnly: true }}
      />

      <TextField
        label="Follow-up Actions"
        multiline
        rows={2}
        fullWidth
        margin="normal"
        value={interactionData.followup}
        InputProps={{ readOnly: true }}
      />

      <TextField
        label="AI Suggested Follow-ups"
        multiline
        rows={2}
        fullWidth
        margin="normal"
        value={
          interactionData.followup
            ? `Follow up with ${interactionData.hcp_name} regarding ${interactionData.topics}.`
            : ""
        }
        InputProps={{ readOnly: true }}
      />
    </Paper>
  );
}