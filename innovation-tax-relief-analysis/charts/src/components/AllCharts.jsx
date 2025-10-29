import React from 'react';
import {
  LineChart, Line, AreaChart, Area, BarChart, Bar, PieChart, Pie,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell
} from 'recharts';
import ChartWrapper from './ChartWrapper';
import { ADDITIONAL_CHARTS } from './AdditionalCharts';
import {
  getBRTimeSeries,
  getBRAmountsTimeSeries,
  getBRBreakdown2024,
  getAllReliefsSummary2024,
  getEcosystemTimeSeries,
  getBRGrowthRates,
  getIPBoxTimeSeries,
  get2022ReliefsTimeSeries,
  getAverageDeductionTimeSeries,
  chartData
} from '../data';

// Inov brand colors
const COLORS = {
  primary: '#ECC246',      // Inov golden yellow
  secondary: '#2C3E50',    // Inov dark navy
  tertiary: '#5BBEC2',     // Turquoise from presentation
  quaternary: '#E86E5E',   // Coral red from presentation
  quinary: '#F9D448',      // Light yellow from presentation
  senary: '#95B8D1',       // Light blue accent
  cit: '#2C3E50',          // Dark navy for CIT
  pit: '#ECC246',          // Golden yellow for PIT
  total: '#5BBEC2'         // Turquoise for totals
};

const PIE_COLORS = ['#2C3E50', '#ECC246', '#5BBEC2', '#E86E5E', '#F9D448', '#95B8D1'];

/**
 * Chart 1: B+R Participant Growth (2017-2024)
 */
export function Chart1_BRParticipantGrowth() {
  const data = getBRTimeSeries();

  return (
    <ChartWrapper
      chartId="chart-01-br-participant-growth"
      title="Wykres 1: Wzrost liczby uczestników ulgi B+R (2017-2024)"
      subtitle="Liczba podmiotów korzystających z ulgi B+R w podziale na CIT i PIT"
    >
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="CIT" stroke={COLORS.cit} strokeWidth={2} name="CIT" />
          <Line type="monotone" dataKey="PIT" stroke={COLORS.pit} strokeWidth={2} name="PIT" />
          <Line type="monotone" dataKey="Total" stroke={COLORS.total} strokeWidth={3} name="Razem" strokeDasharray="5 5" />
        </LineChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 2: B+R Deduction Amounts (2017-2024)
 */
export function Chart2_BRDeductionAmounts() {
  const data = getBRAmountsTimeSeries();

  return (
    <ChartWrapper
      chartId="chart-02-br-deduction-amounts"
      title="Wykres 2: Kwoty odliczeń ulgi B+R (2017-2024)"
      subtitle="Łączne kwoty odliczeń w miliardach PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Miliardy PLN', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Area type="monotone" dataKey="CIT" stackId="1" stroke={COLORS.cit} fill={COLORS.cit} name="CIT" />
          <Area type="monotone" dataKey="PIT" stackId="1" stroke={COLORS.pit} fill={COLORS.pit} name="PIT" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 3: CIT vs PIT Breakdown (2024)
 */
export function Chart3_CITPITBreakdown() {
  const data = getBRBreakdown2024();

  return (
    <ChartWrapper
      chartId="chart-03-cit-pit-breakdown"
      title="Wykres 3: Struktura uczestników ulgi B+R - CIT vs PIT (2024)"
      subtitle="Udział podatników CIT i PIT w łącznej liczbie beneficjentów"
    >
      <ResponsiveContainer width="100%" height={400}>
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            labelLine={true}
            label={({name, value}) => `${name}: ${value.toLocaleString()} (${((value / (data[0].value + data[1].value)) * 100).toFixed(1)}%)`}
            outerRadius={120}
            fill="#8884d8"
            dataKey="value"
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={index === 0 ? COLORS.cit : COLORS.pit} />
            ))}
          </Pie>
          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 4: All 6 Reliefs Comparison (2024)
 */
export function Chart4_AllReliefsComparison() {
  const data = getAllReliefsSummary2024();

  return (
    <ChartWrapper
      chartId="chart-04-all-reliefs-comparison"
      title="Wykres 4: Porównanie wszystkich 6 ulg pro-innowacyjnych (2024)"
      subtitle="Liczba uczestników i kwoty odliczeń"
    >
      <ResponsiveContainer width="100%" height={500}>
        <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 60 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
          <YAxis yAxisId="left" orientation="left" label={{ value: 'Liczba uczestników', angle: -90, position: 'insideLeft' }} />
          <YAxis yAxisId="right" orientation="right" label={{ value: 'Miliardy PLN', angle: 90, position: 'insideRight' }} />
          <Tooltip />
          <Legend />
          <Bar yAxisId="left" dataKey="participants" fill={COLORS.primary} name="Liczba uczestników" />
          <Bar yAxisId="right" dataKey="amount" fill={COLORS.secondary} name="Kwota (mld PLN)" />
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 5: Ecosystem Time Series
 */
export function Chart5_EcosystemTimeSeries() {
  const data = getEcosystemTimeSeries();

  return (
    <ChartWrapper
      chartId="chart-05-ecosystem-time-series"
      title="Wykres 5: Rozwój całego ekosystemu ulg pro-innowacyjnych (2017-2024)"
      subtitle="Łączna liczba uczestników i kwoty odliczeń we wszystkich ulgach"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis yAxisId="left" label={{ value: 'Liczba uczestników', angle: -90, position: 'insideLeft' }} />
          <YAxis yAxisId="right" orientation="right" label={{ value: 'Miliardy PLN', angle: 90, position: 'insideRight' }} />
          <Tooltip />
          <Legend />
          <Area yAxisId="left" type="monotone" dataKey="participants" stroke={COLORS.primary} fill={COLORS.primary} name="Uczestnicy" />
          <Area yAxisId="right" type="monotone" dataKey="amount" stroke={COLORS.secondary} fill={COLORS.secondary} fillOpacity={0.6} name="Kwota (mld PLN)" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 6: B+R Growth Rates
 */
export function Chart6_BRGrowthRates() {
  const rawData = getBRGrowthRates();
  // Filter out 2018 and 2019 completely from X axis
  const data = rawData.filter(item => item.year >= 2020);

  return (
    <ChartWrapper
      chartId="chart-06-br-growth-rates"
      title="Wykres 6: Tempo wzrostu ulgi B+R rok do roku (YoY)"
      subtitle="Procentowy wzrost liczby uczestników i kwot odliczeń (2020-2024)"
    >
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Wzrost (%)', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="participantGrowth" stroke={COLORS.primary} strokeWidth={2} name="Wzrost uczestników (%)" />
          <Line type="monotone" dataKey="amountGrowth" stroke={COLORS.secondary} strokeWidth={2} name="Wzrost kwot (%)" />
        </LineChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 7: IP Box Time Series
 */
export function Chart7_IPBoxTimeSeries() {
  const data = getIPBoxTimeSeries();

  return (
    <ChartWrapper
      chartId="chart-07-ipbox-time-series"
      title="Wykres 7: Rozwój IP Box (2019-2024)"
      subtitle="Liczba uczestników ulgi IP Box w podziale na CIT i PIT"
    >
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="CIT" stroke={COLORS.cit} strokeWidth={2} name="CIT" />
          <Line type="monotone" dataKey="PIT" stroke={COLORS.pit} strokeWidth={2} name="PIT" />
          <Line type="monotone" dataKey="Total" stroke={COLORS.total} strokeWidth={3} name="Razem" strokeDasharray="5 5" />
        </LineChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 8: 2022 Reliefs Comparison
 */
export function Chart8_2022ReliefsComparison() {
  const data = get2022ReliefsTimeSeries();

  return (
    <ChartWrapper
      chartId="chart-08-2022-reliefs-comparison"
      title="Wykres 8: Porównanie ulg wprowadzonych w 2022 roku"
      subtitle="Rozwój liczby uczestników ulg: Robotyzacja, Ekspansja, CSR, Prototyp"
    >
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="Robotyzacja" stroke={COLORS.primary} strokeWidth={2} />
          <Line type="monotone" dataKey="Ekspansja" stroke={COLORS.secondary} strokeWidth={2} />
          <Line type="monotone" dataKey="CSR" stroke={COLORS.tertiary} strokeWidth={2} />
          <Line type="monotone" dataKey="Prototyp" stroke={COLORS.quaternary} strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 9: Average Deduction per Participant
 */
export function Chart9_AverageDeduction() {
  const data = getAverageDeductionTimeSeries();

  return (
    <ChartWrapper
      chartId="chart-09-average-deduction"
      title="Wykres 9: Średnie odliczenie na uczestnika ulgi B+R (2017-2024)"
      subtitle="Średnia kwota odliczenia w tysiącach PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            domain={[0, 3500]}
            label={{ value: 'Tysiące PLN', angle: -90, position: 'insideLeft' }}
          />
          <Tooltip />
          <Legend />
          <Bar dataKey="average" fill={COLORS.tertiary} name="Średnie odliczenie (tys. PLN)" />
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 10: B+R CIT vs PIT by Amount Dominance
 */
export function Chart10_CITDominance() {
  const brData = getBRAmountsTimeSeries();
  const data = brData.map(item => {
    const citAmount = parseFloat(item.CIT);
    const pitAmount = parseFloat(item.PIT);
    const total = citAmount + pitAmount;
    return {
      year: item.year,
      citPercent: parseFloat(((citAmount / total) * 100).toFixed(1)),
      pitPercent: parseFloat(((pitAmount / total) * 100).toFixed(1))
    };
  });

  return (
    <ChartWrapper
      chartId="chart-10-cit-dominance"
      title="Wykres 10: Dominacja CIT w uldze B+R według wartości odliczeń (2017-2024)"
      subtitle="Procentowy udział CIT vs PIT w łącznej wartości odliczeń w PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            label={{ value: 'Procent (%)', angle: -90, position: 'insideLeft' }}
            domain={[0, 100]}
            tickFormatter={(value) => `${value}%`}
          />
          <Tooltip formatter={(value) => `${value}%`} />
          <Legend />
          <Area type="monotone" dataKey="citPercent" stackId="1" stroke={COLORS.cit} fill={COLORS.cit} name="CIT (% wartości)" />
          <Area type="monotone" dataKey="pitPercent" stackId="1" stroke={COLORS.pit} fill={COLORS.pit} name="PIT (% wartości)" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 11: IP Box CIT vs PIT Distribution
 */
export function Chart11_IPBoxDistribution() {
  const data = getIPBoxTimeSeries().map(item => ({
    year: item.year,
    citPercent: ((item.CIT / item.Total) * 100).toFixed(1),
    pitPercent: ((item.PIT / item.Total) * 100).toFixed(1)
  }));

  return (
    <ChartWrapper
      chartId="chart-11-ipbox-distribution"
      title="Wykres 11: Struktura IP Box - CIT vs PIT (2019-2024)"
      subtitle="Udział procentowy CIT i PIT w IP Box (98% to PIT - freelancerzy)"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Procent (%)', angle: -90, position: 'insideLeft' }} domain={[0, 100]} />
          <Tooltip />
          <Legend />
          <Area type="monotone" dataKey="pitPercent" stackId="1" stroke={COLORS.pit} fill={COLORS.pit} name="PIT (%)" />
          <Area type="monotone" dataKey="citPercent" stackId="1" stroke={COLORS.cit} fill={COLORS.cit} name="CIT (%)" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 12: Market Share by Relief (2024)
 */
export function Chart12_MarketShare2024() {
  const data = getAllReliefsSummary2024();

  return (
    <ChartWrapper
      chartId="chart-12-market-share-2024"
      title="Wykres 12: Udział rynkowy poszczególnych ulg w 2024 roku"
      subtitle="Podział kwot odliczeń według typu ulgi"
    >
      <ResponsiveContainer width="100%" height={500}>
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            labelLine={{ stroke: COLORS.secondary, strokeWidth: 1 }}
            label={({name, amount, cx, cy, midAngle, outerRadius}) => {
              const RADIAN = Math.PI / 180;
              const radius = outerRadius + 35;
              const x = cx + radius * Math.cos(-midAngle * RADIAN);
              const y = cy + radius * Math.sin(-midAngle * RADIAN);
              return (
                <text
                  x={x}
                  y={y}
                  fill={COLORS.secondary}
                  textAnchor={x > cx ? 'start' : 'end'}
                  dominantBaseline="central"
                  style={{ fontSize: '12px', fontWeight: '600' }}
                >
                  {`${name}: ${amount.toFixed(2)} mld`}
                </text>
              );
            }}
            outerRadius={110}
            fill="#8884d8"
            dataKey="amount"
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={PIE_COLORS[index % PIE_COLORS.length]} />
            ))}
          </Pie>
          <Tooltip formatter={(value) => `${value.toFixed(2)} mld PLN`} />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

// Export all charts as an array for easy rendering
export const ALL_CHARTS = [
  Chart1_BRParticipantGrowth,
  Chart2_BRDeductionAmounts,
  Chart3_CITPITBreakdown,
  Chart4_AllReliefsComparison,
  Chart5_EcosystemTimeSeries,
  Chart6_BRGrowthRates,
  Chart7_IPBoxTimeSeries,
  Chart8_2022ReliefsComparison,
  Chart9_AverageDeduction,
  Chart10_CITDominance,
  Chart11_IPBoxDistribution,
  Chart12_MarketShare2024,
  ...ADDITIONAL_CHARTS
];
