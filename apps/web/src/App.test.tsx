import { render, screen } from '@testing-library/react';
import { ThemeProvider } from '@mui/material/styles';
import { inovTheme } from './styles/theme';
import App from './App';
import { describe, it, expect } from 'vitest';

describe('App', () => {
  it('renders without crashing', () => {
    render(
      <ThemeProvider theme={inovTheme}>
        <App />
      </ThemeProvider>
    );
    expect(screen.getByText(/Generator Kart Projektów Ulga B\+R/i)).toBeInTheDocument();
  });

  it('applies Inov theme colors', () => {
    render(
      <ThemeProvider theme={inovTheme}>
        <App />
      </ThemeProvider>
    );
    expect(inovTheme.palette.primary.main).toBe('#F5C344');
    expect(inovTheme.palette.secondary.main).toBe('#2C3E50');
  });

  it('renders Tailwind styled box', () => {
    render(
      <ThemeProvider theme={inovTheme}>
        <App />
      </ThemeProvider>
    );
    expect(screen.getByText(/Tailwind CSS działa/i)).toBeInTheDocument();
  });
});
