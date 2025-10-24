import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ThemeProvider } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'
import { inovTheme } from './styles/theme'
import './styles/globals.css'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ThemeProvider theme={inovTheme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </StrictMode>,
)
