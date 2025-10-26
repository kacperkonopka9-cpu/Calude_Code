import React from 'react';
import { ALL_CHARTS } from './components/AllCharts';
import './App.css';

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <img src="/inov-logo.png" alt="Inov Research & Development" className="inov-logo" />
        <h1>Wizualizacje danych: Polskie ulgi pro-innowacyjne</h1>
        <p className="subtitle">Analiza ulg podatkowych B+R, IP Box, Robotyzacja, Ekspansja, CSR i Prototyp (2017-2024)</p>
        <p className="data-source">
          Źródło danych: Ministerstwo Finansów (KAS), stan na 14.10.2025
        </p>
      </header>

      <main className="charts-container">
        {ALL_CHARTS.map((ChartComponent, index) => (
          <ChartComponent key={index} />
        ))}
      </main>

      <footer className="app-footer">
        <div className="inov-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <p>
          Dane pochodzą z oficjalnych statystyk Ministerstwa Finansów (Krajowa Administracja Skarbowa).
          <br />
          Raport: "Analiza ekosystemu ulg pro-innowacyjnych i luki w raportowaniu statystycznym"
        </p>
        <p style={{ marginTop: '16px', fontSize: '13px', opacity: 0.7 }}>
          Opracowanie: <strong>Inov Research & Development</strong>
        </p>
      </footer>
    </div>
  );
}

export default App;
