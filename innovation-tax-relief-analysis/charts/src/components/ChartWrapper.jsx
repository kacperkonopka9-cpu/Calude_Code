import React, { useRef } from 'react';
import { toPng } from 'html-to-image';

/**
 * Wrapper component for all charts with consistent styling and export functionality
 */
export default function ChartWrapper({ title, subtitle, children, chartId }) {
  const chartRef = useRef(null);

  const handleExport = async () => {
    if (chartRef.current === null) return;

    try {
      const dataUrl = await toPng(chartRef.current, {
        cacheBust: true,
        pixelRatio: 3, // 300 DPI equivalent
        backgroundColor: '#ffffff'
      });

      const link = document.createElement('a');
      link.download = `${chartId}.png`;
      link.href = dataUrl;
      link.click();
    } catch (err) {
      console.error('Failed to export chart:', err);
    }
  };

  return (
    <div style={{ marginBottom: '40px', pageBreakInside: 'avoid' }}>
      <div
        ref={chartRef}
        style={{
          padding: '24px',
          backgroundColor: '#ffffff',
          border: '3px solid #ECC246',
          borderRadius: '12px',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.08)'
        }}
      >
        <div style={{ marginBottom: '20px' }}>
          <h2 style={{
            fontSize: '18px',
            fontWeight: 'bold',
            marginBottom: '8px',
            color: '#2C3E50'
          }}>
            {title}
          </h2>
          {subtitle && (
            <p style={{
              fontSize: '14px',
              color: '#5A5A5A',
              marginBottom: '0'
            }}>
              {subtitle}
            </p>
          )}
        </div>
        {children}
      </div>
      <button
        onClick={handleExport}
        style={{
          marginTop: '12px',
          padding: '10px 20px',
          backgroundColor: '#ECC246',
          color: '#2C3E50',
          border: '2px solid #2C3E50',
          borderRadius: '6px',
          cursor: 'pointer',
          fontSize: '14px',
          fontWeight: '600',
          transition: 'all 0.2s ease'
        }}
        onMouseOver={(e) => {
          e.target.style.backgroundColor = '#2C3E50';
          e.target.style.color = '#ECC246';
        }}
        onMouseOut={(e) => {
          e.target.style.backgroundColor = '#ECC246';
          e.target.style.color = '#2C3E50';
        }}
      >
        Eksportuj jako PNG
      </button>
    </div>
  );
}
