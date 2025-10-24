import { useState } from 'react'
import { Button, Container, Typography, Box } from '@mui/material'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Container maxWidth="md">
      <Box sx={{ textAlign: 'center', mt: 8 }}>
        <Typography variant="h2" component="h1" gutterBottom>
          Generator Kart Projektów Ulga B+R
        </Typography>
        <Typography variant="h5" component="h2" color="text.secondary" gutterBottom>
          Witamy w Inov Research & Development
        </Typography>
        <Box sx={{ mt: 4 }}>
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={() => setCount((count) => count + 1)}
          >
            Licznik: {count}
          </Button>
        </Box>
        <Typography variant="body1" sx={{ mt: 4 }}>
          Edytuj <code>src/App.tsx</code> i zapisz, aby przetestować HMR
        </Typography>
        <Box className="mt-4 p-4 bg-inov-yellow text-inov-navy rounded-lg">
          <Typography variant="body2">
            Tailwind CSS działa! To pole używa kolorów marki Inov.
          </Typography>
        </Box>
      </Box>
    </Container>
  )
}

export default App
