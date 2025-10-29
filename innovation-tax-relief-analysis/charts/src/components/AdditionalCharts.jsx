import React from 'react';
import {
  LineChart, Line, AreaChart, Area, BarChart, Bar, ComposedChart,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell
} from 'recharts';
import ChartWrapper from './ChartWrapper';
import { chartData } from '../data';

// Inov brand colors
const COLORS = {
  primary: '#ECC246',      // Inov golden yellow
  secondary: '#2C3E50',    // Inov dark navy
  tertiary: '#5BBEC2',     // Turquoise from presentation
  quaternary: '#E86E5E',   // Coral red from presentation
  quinary: '#F9D448',      // Light yellow from presentation
  senary: '#95B8D1'        // Light blue accent
};

/**
 * Chart 13: B+R CIT Amount Growth
 */
export function Chart13_BRCITAmountGrowth() {
  const { br } = chartData;
  const data = br.years.map((year, i) => ({
    year,
    amount: (br.cit.amounts[i] / 1000000000).toFixed(2)
  }));

  return (
    <ChartWrapper
      chartId="chart-13-br-cit-amount-growth"
      title="Wykres 13: Wzrost kwot odliczeń CIT w uldze B+R (2017-2024)"
      subtitle="Kwoty odliczeń tylko dla podatników CIT w miliardach PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Miliardy PLN', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Area type="monotone" dataKey="amount" stroke={COLORS.primary} fill={COLORS.primary} name="CIT (mld PLN)" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 14: B+R PIT Amount Growth
 */
export function Chart14_BRPITAmountGrowth() {
  const { br } = chartData;
  const data = br.years.map((year, i) => ({
    year,
    amount: (br.pit.amounts[i] / 1000000000).toFixed(2)
  }));

  return (
    <ChartWrapper
      chartId="chart-14-br-pit-amount-growth"
      title="Wykres 14: Wzrost kwot odliczeń PIT w uldze B+R (2017-2024)"
      subtitle="Kwoty odliczeń tylko dla podatników PIT w miliardach PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Miliardy PLN', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Area type="monotone" dataKey="amount" stroke={COLORS.secondary} fill={COLORS.secondary} name="PIT (mld PLN)" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 15: IP Box Amount Distribution (2024)
 */
export function Chart15_IPBoxAmountDistribution() {
  const { ipbox } = chartData;
  const idx = ipbox.years.indexOf(2024);
  const data = ipbox.years.map((year, i) => ({
    year,
    CIT: (ipbox.cit.amounts[i] / 1000000).toFixed(2),
    PIT: (ipbox.pit.amounts[i] / 1000000).toFixed(2)
  }));

  return (
    <ChartWrapper
      chartId="chart-15-ipbox-amount-distribution"
      title="Wykres 15: Kwoty odliczeń IP Box (2019-2024)"
      subtitle="Porównanie kwot CIT i PIT w milionach PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Miliony PLN', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Bar dataKey="CIT" fill={COLORS.primary} name="CIT (mln PLN)" />
          <Bar dataKey="PIT" fill={COLORS.secondary} name="PIT (mln PLN)" />
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 15: 2022 Reliefs Amount Comparison
 */
export function Chart15_2022ReliefsAmountComparison() {
  const { reliefs_2022 } = chartData;
  const years = reliefs_2022.prototyp.years;

  const data = years.map((year, i) => ({
    year,
    Robotyzacja: parseFloat(((reliefs_2022.robotyzacja.cit.amounts[i] + reliefs_2022.robotyzacja.pit.amounts[i]) / 1000000).toFixed(2)),
    Ekspansja: parseFloat(((reliefs_2022.ekspansja.cit.amounts[i] + reliefs_2022.ekspansja.pit.amounts[i]) / 1000000).toFixed(2)),
    CSR: parseFloat(((reliefs_2022.csr.cit.amounts[i] + reliefs_2022.csr.pit.amounts[i]) / 1000000).toFixed(2)),
    Prototyp: parseFloat(((reliefs_2022.prototyp.cit.amounts[i] + reliefs_2022.prototyp.pit.amounts[i]) / 1000000).toFixed(2))
  }));

  return (
    <ChartWrapper
      chartId="chart-15-2022-reliefs-amount-comparison"
      title="Wykres 15: Kwoty odliczeń ulg wprowadzonych w 2022 roku"
      subtitle="Porównanie wartości odliczeń w milionach PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            domain={[0, 600]}
            label={{ value: 'Miliony PLN', angle: -90, position: 'insideLeft' }}
          />
          <Tooltip />
          <Legend />
          <Bar dataKey="Robotyzacja" fill={COLORS.primary} name="Robotyzacja" />
          <Bar dataKey="Ekspansja" fill={COLORS.secondary} name="Ekspansja" />
          <Bar dataKey="CSR" fill={COLORS.tertiary} name="CSR" />
          <Bar dataKey="Prototyp" fill={COLORS.quaternary} name="Prototyp" />
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 17: CSR Growth Trend
 */
export function Chart16_CSRGrowthTrend() {
  const { reliefs_2022 } = chartData;
  const data = reliefs_2022.csr.years.map((year, i) => ({
    year,
    participants: reliefs_2022.csr.cit.counts[i] + reliefs_2022.csr.pit.counts[i],
    amount: parseFloat(((reliefs_2022.csr.cit.amounts[i] + reliefs_2022.csr.pit.amounts[i]) / 1000000).toFixed(2))
  }));

  return (
    <ChartWrapper
      chartId="chart-16-csr-growth-trend"
      title="Wykres 16: Dynamiczny wzrost ulgi CSR (2022-2024)"
      subtitle="Najszybciej rosnąca ulga spośród instrumentów wprowadzonych w 2022"
    >
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            yAxisId="left"
            domain={[0, 3000]}
            label={{ value: 'Liczba uczestników', angle: -90, position: 'insideLeft' }}
          />
          <YAxis
            yAxisId="right"
            orientation="right"
            domain={[0, 160]}
            label={{ value: 'Miliony PLN', angle: 90, position: 'insideRight' }}
          />
          <Tooltip />
          <Legend />
          <Bar yAxisId="left" dataKey="participants" fill={COLORS.tertiary} name="Uczestnicy" />
          <Line yAxisId="right" type="monotone" dataKey="amount" stroke={COLORS.secondary} strokeWidth={3} name="Kwota (mln PLN)" />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 18: Robotyzacja Trend
 */
export function Chart17_RobotyzacjaTrend() {
  const { reliefs_2022 } = chartData;
  const data = reliefs_2022.robotyzacja.years.map((year, i) => ({
    year,
    participants: reliefs_2022.robotyzacja.cit.counts[i] + reliefs_2022.robotyzacja.pit.counts[i],
    amount: parseFloat(((reliefs_2022.robotyzacja.cit.amounts[i] + reliefs_2022.robotyzacja.pit.amounts[i]) / 1000000).toFixed(2))
  }));

  return (
    <ChartWrapper
      chartId="chart-17-robotyzacja-trend"
      title="Wykres 17: Rozwój ulgi na robotyzację (2022-2024)"
      subtitle="Największa wartość odliczeń spośród ulg wprowadzonych w 2022"
    >
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            yAxisId="left"
            domain={[0, 500]}
            label={{ value: 'Liczba uczestników', angle: -90, position: 'insideLeft' }}
          />
          <YAxis
            yAxisId="right"
            orientation="right"
            domain={[0, 600]}
            label={{ value: 'Miliony PLN', angle: 90, position: 'insideRight' }}
          />
          <Tooltip />
          <Legend />
          <Bar yAxisId="left" dataKey="participants" fill={COLORS.primary} name="Uczestnicy" />
          <Line yAxisId="right" type="monotone" dataKey="amount" stroke={COLORS.secondary} strokeWidth={3} name="Kwota (mln PLN)" />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 19: Prototyp Decline
 */
export function Chart18_PrototypDecline() {
  const { reliefs_2022 } = chartData;
  const data = reliefs_2022.prototyp.years.map((year, i) => ({
    year,
    participants: reliefs_2022.prototyp.cit.counts[i] + reliefs_2022.prototyp.pit.counts[i],
    amount: ((reliefs_2022.prototyp.cit.amounts[i] + reliefs_2022.prototyp.pit.amounts[i]) / 1000000).toFixed(2)
  }));

  return (
    <ChartWrapper
      chartId="chart-18-prototyp-decline"
      title="Wykres 18: Spadek popularności ulgi na prototyp (2022-2024)"
      subtitle="Najmniejsza i malejąca liczba uczestników"
    >
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis yAxisId="left" label={{ value: 'Liczba uczestników', angle: -90, position: 'insideLeft' }} />
          <YAxis yAxisId="right" orientation="right" label={{ value: 'Miliony PLN', angle: 90, position: 'insideRight' }} />
          <Tooltip />
          <Legend />
          <Bar yAxisId="left" dataKey="participants" fill={COLORS.quaternary} name="Uczestnicy" />
          <Line yAxisId="right" type="monotone" dataKey="amount" stroke={COLORS.secondary} strokeWidth={3} name="Kwota (mln PLN)" />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 20: Cumulative Participants All Reliefs
 */
export function Chart19_CumulativeParticipantsAllReliefs() {
  const { totals } = chartData;
  const cumulativeData = [];
  let runningTotal = 0;

  totals.cumulative.years.forEach((year, i) => {
    runningTotal += totals.cumulative.counts[i];
    cumulativeData.push({
      year,
      cumulative: runningTotal
    });
  });

  return (
    <ChartWrapper
      chartId="chart-19-cumulative-participants"
      title="Wykres 19: Skumulowana liczba beneficjentów (2017-2024)"
      subtitle="Łączna suma wszystkich uczestników przez lata (entity-years)"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={cumulativeData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Skumulowana liczba', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Area type="monotone" dataKey="cumulative" stroke={COLORS.primary} fill={COLORS.primary} name="Suma beneficjentów" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 21: Cumulative Amounts All Reliefs
 */
export function Chart21_CumulativeAmountsAllReliefs() {
  const { totals } = chartData;
  const cumulativeData = [];
  let runningTotal = 0;

  totals.cumulative.years.forEach((year, i) => {
    runningTotal += totals.cumulative.amounts[i];
    cumulativeData.push({
      year,
      cumulative: (runningTotal / 1000000000).toFixed(2)
    });
  });

  return (
    <ChartWrapper
      chartId="chart-21-cumulative-amounts"
      title="Wykres 21: Skumulowane kwoty odliczeń (2017-2024)"
      subtitle="Łączna suma odliczeń we wszystkich ulgach w miliardach PLN"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={cumulativeData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Miliardy PLN', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Area type="monotone" dataKey="cumulative" stroke={COLORS.secondary} fill={COLORS.secondary} name="Skumulowane kwoty (mld PLN)" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 22: Grant Thornton vs Ministry Comparison (Statistical Gap)
 */
export function Chart20_GrantThorntonVsMinistryGap() {
  // Difference data: Grant Thornton historical vs Ministry of Finance corrected data
  // This shows the "Różnica" - unreported R&D work to OECD
  const citData = [
    { year: 2017, participants: 163, amount: (234942142.87 / 1000000).toFixed(2) },
    { year: 2018, participants: 635, amount: (1117274171.38 / 1000000).toFixed(2) },
    { year: 2019, participants: 620, amount: (895103060.38 / 1000000).toFixed(2) },
    { year: 2020, participants: 725, amount: (1438071557.42 / 1000000).toFixed(2) },
    { year: 2021, participants: 754, amount: (1344808440.37 / 1000000).toFixed(2) },
    { year: 2022, participants: 670, amount: (2167663321.18 / 1000000).toFixed(2) },
    { year: 2023, participants: 440, amount: (2011802993.43 / 1000000).toFixed(2) },
    { year: 2024, participants: 94, amount: (467254504.26 / 1000000).toFixed(2) }
  ];

  const pitData = [
    { year: 2017, participants: 189, amount: (45371223.26 / 1000000).toFixed(2) },
    { year: 2018, participants: 683, amount: (262129545.69 / 1000000).toFixed(2) },
    { year: 2019, participants: 674, amount: (231794596.66 / 1000000).toFixed(2) },
    { year: 2020, participants: 638, amount: (243610926.70 / 1000000).toFixed(2) },
    { year: 2021, participants: 429, amount: (130376331.97 / 1000000).toFixed(2) },
    { year: 2022, participants: 410, amount: (114516560.65 / 1000000).toFixed(2) },
    { year: 2023, participants: 1146, amount: (57288351.80 / 1000000).toFixed(2) },
    { year: 2024, participants: 20, amount: (15098035.14 / 1000000).toFixed(2) }
  ];

  const combinedData = citData.map((cit, i) => ({
    year: cit.year,
    citParticipants: cit.participants,
    pitParticipants: pitData[i].participants,
    totalParticipants: cit.participants + pitData[i].participants,
    citAmount: parseFloat(cit.amount),
    pitAmount: parseFloat(pitData[i].amount),
    totalAmount: parseFloat(cit.amount) + parseFloat(pitData[i].amount)
  }));

  return (
    <ChartWrapper
      chartId="chart-20-grant-thornton-ministry-gap"
      title="Wykres 20: Luka statystyczna B+R - różnica między danymi Grant Thornton a MF"
      subtitle="Wartość nieraportowanych prac B+R do OECD (w milionach PLN)"
    >
      <ResponsiveContainer width="100%" height={450}>
        <ComposedChart data={combinedData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            yAxisId="left"
            domain={[0, 2000]}
            label={{ value: 'Liczba podmiotów', angle: -90, position: 'insideLeft' }}
          />
          <YAxis
            yAxisId="right"
            orientation="right"
            domain={[0, 3000]}
            label={{ value: 'Miliony PLN', angle: 90, position: 'insideRight' }}
          />
          <Tooltip />
          <Legend />
          <Bar yAxisId="left" dataKey="citParticipants" stackId="a" fill={COLORS.secondary} name="CIT - Liczba podmiotów" />
          <Bar yAxisId="left" dataKey="pitParticipants" stackId="a" fill={COLORS.primary} name="PIT - Liczba podmiotów" />
          <Line yAxisId="right" type="monotone" dataKey="totalAmount" stroke={COLORS.quaternary} strokeWidth={3} name="Łączna kwota (mln PLN)" />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 23: Statistical Gap Trend Over Time
 */
export function Chart21_StatisticalGapTrend() {
  const data = [
    { year: 2017, participants: 352, amount: 280.31 },
    { year: 2018, participants: 1318, amount: 1379.40 },
    { year: 2019, participants: 1294, amount: 1126.90 },
    { year: 2020, participants: 1363, amount: 1681.68 },
    { year: 2021, participants: 1183, amount: 1475.18 },
    { year: 2022, participants: 1080, amount: 2282.18 },
    { year: 2023, participants: 1586, amount: 2069.09 },
    { year: 2024, participants: 114, amount: 482.35 }
  ];

  return (
    <ChartWrapper
      chartId="chart-21-statistical-gap-trend"
      title="Wykres 21: Trend luki statystycznej w czasie (2017-2024)"
      subtitle="Liczba podmiotów i wartość nieraportowanych prac B+R"
    >
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            yAxisId="left"
            label={{ value: 'Liczba podmiotów', angle: -90, position: 'insideLeft' }}
          />
          <YAxis
            yAxisId="right"
            orientation="right"
            label={{ value: 'Miliony PLN', angle: 90, position: 'insideRight' }}
          />
          <Tooltip />
          <Legend />
          <Bar yAxisId="left" dataKey="participants" fill={COLORS.tertiary} name="Podmioty (luka)" />
          <Line yAxisId="right" type="monotone" dataKey="amount" stroke={COLORS.quaternary} strokeWidth={3} name="Kwota (mln PLN)" />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 24: Total Hidden Reporting Amount Per Year
 */
export function Chart22_TotalHiddenReportingPerYear() {
  const data = [
    { year: 2017, amount: 280.31 },
    { year: 2018, amount: 1379.40 },
    { year: 2019, amount: 1240.55 },
    { year: 2020, amount: 1830.94 },
    { year: 2021, amount: 1525.29 },
    { year: 2022, amount: 2472.90 },
    { year: 2023, amount: 2390.53 },
    { year: 2024, amount: 653.92 }
  ];

  return (
    <ChartWrapper
      chartId="chart-22-total-hidden-reporting-per-year"
      title="Wykres 22: Suma ukrytego raportowania per rok (2017-2024)"
      subtitle="Łączna wartość nieraportowanych prac B+R (mln PLN)"
    >
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            domain={[0, 2600]}
            label={{ value: 'Miliony PLN', angle: -90, position: 'insideLeft' }}
          />
          <Tooltip formatter={(value) => `${value.toFixed(2)} mln PLN`} />
          <Legend />
          <Bar dataKey="amount" fill={COLORS.quaternary} name="Suma ukrytego raportowania (mln PLN)" />
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 25: Gap Percentage Analysis - Participants
 */
export function Chart24_GapPercentageParticipants() {
  // Need to calculate % gap = (gap_count / (official_count + gap_count)) * 100
  const officialData = [
    { year: 2017, official: 1508 }, // 795 CIT + 713 PIT
    { year: 2018, official: 3324 }, // 1748 + 1576
    { year: 2019, official: 3923 }, // 2054 + 1869
    { year: 2020, official: 4493 }, // 2368 + 2125
    { year: 2021, official: 4741 }, // 2791 + 1950
    { year: 2022, official: 4414 }, // 2961 + 1453
    { year: 2023, official: 4102 }, // 2841 + 1261
    { year: 2024, official: 3655 }  // 2544 + 1111
  ];

  const gapData = [352, 1318, 1294, 1363, 1183, 1080, 1586, 114];

  const data = officialData.map((item, i) => {
    const total = item.official + gapData[i];
    const gapPercent = ((gapData[i] / total) * 100).toFixed(1);
    return {
      year: item.year,
      gapPercent: parseFloat(gapPercent),
      officialPercent: parseFloat((100 - gapPercent).toFixed(1))
    };
  });

  return (
    <ChartWrapper
      chartId="chart-24-gap-percentage-participants"
      title="Wykres 24: Procentowa luka w liczbie uczestników B+R (2017-2024)"
      subtitle="% podmiotów korzystających z ulgi B+R, które nie raportują do GUS"
    >
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis
            domain={[0, 100]}
            label={{ value: 'Procent (%)', angle: -90, position: 'insideLeft' }}
            tickFormatter={(value) => `${value}%`}
          />
          <Tooltip formatter={(value) => `${value}%`} />
          <Legend />
          <Area type="monotone" dataKey="officialPercent" stackId="1" stroke={COLORS.tertiary} fill={COLORS.tertiary} name="Raportowane (%)" />
          <Area type="monotone" dataKey="gapPercent" stackId="1" stroke={COLORS.quaternary} fill={COLORS.quaternary} name="Luka statystyczna (%)" />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 26: CIT vs PIT Gap Comparison
 */
export function Chart25_CITPITGapComparison() {
  const citGap = [
    { year: 2017, amount: 234.94 },
    { year: 2018, amount: 1117.27 },
    { year: 2019, amount: 895.10 },
    { year: 2020, amount: 1438.07 },
    { year: 2021, amount: 1344.81 },
    { year: 2022, amount: 2167.66 },
    { year: 2023, amount: 2011.80 },
    { year: 2024, amount: 467.25 }
  ];

  const pitGap = [
    { year: 2017, amount: 45.37 },
    { year: 2018, amount: 262.13 },
    { year: 2019, amount: 231.79 },
    { year: 2020, amount: 243.61 },
    { year: 2021, amount: 130.38 },
    { year: 2022, amount: 114.52 },
    { year: 2023, amount: 57.29 },
    { year: 2024, amount: 15.10 }
  ];

  const data = citGap.map((cit, i) => ({
    year: cit.year,
    CIT: cit.amount,
    PIT: pitGap[i].amount
  }));

  return (
    <ChartWrapper
      chartId="chart-25-cit-pit-gap-comparison"
      title="Wykres 25: Luka statystyczna CIT vs PIT (2017-2024)"
      subtitle="Porównanie nieraportowanych kwot według typu podatnika (mln PLN)"
    >
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis label={{ value: 'Miliony PLN', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Bar dataKey="CIT" fill={COLORS.secondary} name="CIT (luka, mln PLN)" />
          <Bar dataKey="PIT" fill={COLORS.primary} name="PIT (luka, mln PLN)" />
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

/**
 * Chart 23: Hidden Reporting by Tax Relief Type (Dual Y-Axis) - Completely rebuilt
 */
export function Chart23_HiddenReportingByRelief() {
  // Define colors for each relief type
  const reliefColors = {
    'B+R': '#2C3E50',        // Dark Navy
    'CSR': '#5BBEC2',        // Turquoise
    'IP Box': '#ECC246',     // Golden Yellow
    'Robotyzacja': '#E86E5E', // Coral Red
    'Ekspansja': '#9370DB',  // Medium Purple
    'Prototyp': '#66A182'    // Sage Green
  };

  // Simple data structure: one row per relief type with its amount
  // B+R uses left Y-axis, others use right Y-axis
  const data = [
    { name: 'B+R', amount: 10777.11, yAxisId: 'left' },
    { name: 'CSR', amount: 356.90, yAxisId: 'right' },
    { name: 'IP Box', amount: 348.14, yAxisId: 'right' },
    { name: 'Robotyzacja', amount: 203.06, yAxisId: 'right' },
    { name: 'Ekspansja', amount: 74.14, yAxisId: 'right' },
    { name: 'Prototyp', amount: 14.49, yAxisId: 'right' }
  ];

  // For dual Y-axis, we need separate data arrays
  const leftData = data.map(item => ({
    name: item.name,
    leftAmount: item.yAxisId === 'left' ? item.amount : null
  }));

  const rightData = data.map(item => ({
    name: item.name,
    rightAmount: item.yAxisId === 'right' ? item.amount : null
  }));

  // Merge both datasets
  const mergedData = data.map((item, idx) => ({
    name: item.name,
    leftAmount: leftData[idx].leftAmount,
    rightAmount: rightData[idx].rightAmount
  }));

  return (
    <ChartWrapper
      chartId="chart-23-hidden-reporting-by-relief"
      title="Wykres 23: Suma ukrytego raportowania per ulgę (2017-2024)"
      subtitle="Łączna wartość nieraportowanych prac według typu ulgi (mln PLN)"
    >
      <ResponsiveContainer width="100%" height={550}>
        <BarChart
          data={mergedData}
          margin={{ top: 20, right: 90, left: 60, bottom: 80 }}
          barCategoryGap="20%"
          barGap={0}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="name"
            angle={0}
            textAnchor="middle"
            height={60}
            style={{ fontSize: '13px', fontWeight: 500 }}
            interval={0}
          />
          <YAxis
            yAxisId="left"
            domain={[0, 12000]}
            label={{
              value: 'B+R (mln PLN)',
              angle: -90,
              position: 'insideLeft',
              style: { fontSize: '13px', fontWeight: 600 }
            }}
            style={{ fontSize: '12px' }}
          />
          <YAxis
            yAxisId="right"
            orientation="right"
            domain={[0, 400]}
            label={{
              value: 'Pozostałe ulgi (mln PLN)',
              angle: 90,
              position: 'insideRight',
              offset: 20,
              style: { fontSize: '13px', fontWeight: 600 }
            }}
            style={{ fontSize: '12px' }}
          />
          <Tooltip
            formatter={(value, name) => {
              if (value === null) return null;
              return [`${value.toFixed(2)} mln PLN`, name === 'leftAmount' ? 'B+R' : 'Kwota'];
            }}
            contentStyle={{ fontSize: '13px' }}
          />
          <Legend
            payload={[
              { value: 'B+R', type: 'rect', color: reliefColors['B+R'] },
              { value: 'CSR', type: 'rect', color: reliefColors['CSR'] },
              { value: 'IP Box', type: 'rect', color: reliefColors['IP Box'] },
              { value: 'Robotyzacja', type: 'rect', color: reliefColors['Robotyzacja'] },
              { value: 'Ekspansja', type: 'rect', color: reliefColors['Ekspansja'] },
              { value: 'Prototyp', type: 'rect', color: reliefColors['Prototyp'] }
            ]}
            verticalAlign="bottom"
            align="center"
            wrapperStyle={{ paddingTop: '15px', fontSize: '12px' }}
            iconSize={10}
          />
          <Bar yAxisId="left" dataKey="leftAmount" barSize={120}>
            {mergedData.map((entry, index) => (
              <Cell key={`cell-left-${index}`} fill={entry.leftAmount !== null ? reliefColors[entry.name] : 'transparent'} />
            ))}
          </Bar>
          <Bar yAxisId="right" dataKey="rightAmount" barSize={120}>
            {mergedData.map((entry, index) => (
              <Cell key={`cell-right-${index}`} fill={entry.rightAmount !== null ? reliefColors[entry.name] : 'transparent'} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}

// Export all additional charts (excluding deleted Chart 15 and Chart 21)
export const ADDITIONAL_CHARTS = [
  Chart13_BRCITAmountGrowth,
  Chart14_BRPITAmountGrowth,
  // Chart15_IPBoxAmountDistribution - DELETED per user request
  Chart15_2022ReliefsAmountComparison,
  Chart16_CSRGrowthTrend,
  Chart17_RobotyzacjaTrend,
  Chart18_PrototypDecline,
  Chart19_CumulativeParticipantsAllReliefs,
  // Chart21_CumulativeAmountsAllReliefs - DELETED per user request
  Chart20_GrantThorntonVsMinistryGap,  // Statistical gap: raw data comparison
  Chart21_StatisticalGapTrend,         // NEW: Gap trend over time
  Chart22_TotalHiddenReportingPerYear, // NEW: Total hidden reporting per year
  Chart23_HiddenReportingByRelief,     // NEW: Hidden reporting by tax relief type
  Chart24_GapPercentageParticipants,   // NEW: % gap in participants
  Chart25_CITPITGapComparison          // NEW: CIT vs PIT gap comparison
];
