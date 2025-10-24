import { useState } from 'react'
import { Button, Container, Typography, Box } from '@mui/material'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Container maxWidth="md">
      <Box sx={{ textAlign: 'center', mt: 8 }}>
        <Typography variant="h2" component="h1" gutterBottom>
          R&D Tax Relief Generator
        </Typography>
        <Typography variant="h5" component="h2" color="text.secondary" gutterBottom>
          Welcome to iNOV Research & Development
        </Typography>
        <Box sx={{ mt: 4 }}>
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={() => setCount((count) => count + 1)}
          >
            Count is {count}
          </Button>
        </Box>
        <Typography variant="body1" sx={{ mt: 4 }}>
          Edit <code>src/App.tsx</code> and save to test HMR
        </Typography>
        <Box className="mt-4 p-4 bg-inov-yellow text-inov-navy rounded-lg">
          <Typography variant="body2">
            Tailwind CSS is working! This box uses custom iNOV colors.
          </Typography>
        </Box>
      </Box>
    </Container>
  )
}

export default App
