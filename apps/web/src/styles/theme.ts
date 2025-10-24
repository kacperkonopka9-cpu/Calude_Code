import { createTheme } from '@mui/material/styles';

/**
 * iNOV Research & Development Brand Theme
 * Primary: Yellow #F5C344 (CTAs, highlights, accents)
 * Secondary: Navy #2C3E50 (text, headers, navigation)
 */
export const inovTheme = createTheme({
  palette: {
    primary: {
      main: '#F5C344', // Yellow
    },
    secondary: {
      main: '#2C3E50', // Navy
    },
  },
  typography: {
    fontFamily: 'Inter, sans-serif',
    h1: { fontFamily: 'Roboto Slab, serif' },
    h2: { fontFamily: 'Roboto Slab, serif' },
    h3: { fontFamily: 'Roboto Slab, serif' },
    h4: { fontFamily: 'Roboto Slab, serif' },
    h5: { fontFamily: 'Roboto Slab, serif' },
    h6: { fontFamily: 'Roboto Slab, serif' },
  },
});
