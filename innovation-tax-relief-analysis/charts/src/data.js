/**
 * Data loading and transformation utilities
 */

// Import the chart data
import chartDataJson from '../../data/chart-data.json';

export const chartData = chartDataJson;

/**
 * Transform B+R data for time series charts
 */
export function getBRTimeSeries() {
  const { br } = chartData;
  return br.years.map((year, i) => ({
    year,
    CIT: br.cit.counts[i],
    PIT: br.pit.counts[i],
    Total: br.cit.counts[i] + br.pit.counts[i]
  }));
}

/**
 * Transform B+R amounts for time series charts
 */
export function getBRAmountsTimeSeries() {
  const { br } = chartData;
  return br.years.map((year, i) => ({
    year,
    CIT: (br.cit.amounts[i] / 1000000000).toFixed(2), // Convert to billions
    PIT: (br.pit.amounts[i] / 1000000000).toFixed(2),
    Total: ((br.cit.amounts[i] + br.pit.amounts[i]) / 1000000000).toFixed(2)
  }));
}

/**
 * Get CIT vs PIT breakdown for 2024
 */
export function getBRBreakdown2024() {
  const { br } = chartData;
  const idx = br.years.indexOf(2024);
  return [
    { name: 'CIT', value: br.cit.counts[idx], amount: br.cit.amounts[idx] },
    { name: 'PIT', value: br.pit.counts[idx], amount: br.pit.amounts[idx] }
  ];
}

/**
 * Get all 6 reliefs summary for 2024
 */
export function getAllReliefsSummary2024() {
  const { br, ipbox, reliefs_2022 } = chartData;

  const brIdx = br.years.indexOf(2024);
  const ipboxIdx = ipbox.years.indexOf(2024);
  const reliefs2022Idx = 2; // 2024 is index 2 in 2022-2024 array

  return [
    {
      name: 'B+R',
      participants: br.cit.counts[brIdx] + br.pit.counts[brIdx],
      amount: (br.cit.amounts[brIdx] + br.pit.amounts[brIdx]) / 1000000000
    },
    {
      name: 'IP Box',
      participants: ipbox.cit.counts[ipboxIdx] + ipbox.pit.counts[ipboxIdx],
      amount: (ipbox.cit.amounts[ipboxIdx] + ipbox.pit.amounts[ipboxIdx]) / 1000000000
    },
    {
      name: 'Robotyzacja',
      participants: reliefs_2022.robotyzacja.cit.counts[reliefs2022Idx] + reliefs_2022.robotyzacja.pit.counts[reliefs2022Idx],
      amount: (reliefs_2022.robotyzacja.cit.amounts[reliefs2022Idx] + reliefs_2022.robotyzacja.pit.amounts[reliefs2022Idx]) / 1000000000
    },
    {
      name: 'CSR',
      participants: reliefs_2022.csr.cit.counts[reliefs2022Idx] + reliefs_2022.csr.pit.counts[reliefs2022Idx],
      amount: (reliefs_2022.csr.cit.amounts[reliefs2022Idx] + reliefs_2022.csr.pit.amounts[reliefs2022Idx]) / 1000000000
    },
    {
      name: 'Ekspansja',
      participants: reliefs_2022.ekspansja.cit.counts[reliefs2022Idx] + reliefs_2022.ekspansja.pit.counts[reliefs2022Idx],
      amount: (reliefs_2022.ekspansja.cit.amounts[reliefs2022Idx] + reliefs_2022.ekspansja.pit.amounts[reliefs2022Idx]) / 1000000000
    },
    {
      name: 'Prototyp',
      participants: reliefs_2022.prototyp.cit.counts[reliefs2022Idx] + reliefs_2022.prototyp.pit.counts[reliefs2022Idx],
      amount: (reliefs_2022.prototyp.cit.amounts[reliefs2022Idx] + reliefs_2022.prototyp.pit.amounts[reliefs2022Idx]) / 1000000000
    }
  ];
}

/**
 * Get cumulative ecosystem data
 */
export function getEcosystemTimeSeries() {
  const { totals } = chartData;
  return totals.cumulative.years.map((year, i) => ({
    year,
    participants: totals.cumulative.counts[i],
    amount: (totals.cumulative.amounts[i] / 1000000000).toFixed(2)
  }));
}

/**
 * Get growth rates for B+R
 */
export function getBRGrowthRates() {
  const { growth } = chartData;
  return growth.br.years.map((year, i) => ({
    year,
    participantGrowth: growth.br.count_growth[i],
    amountGrowth: growth.br.amount_growth[i]
  }));
}

/**
 * Get IP Box time series
 */
export function getIPBoxTimeSeries() {
  const { ipbox } = chartData;
  return ipbox.years.map((year, i) => ({
    year,
    CIT: ipbox.cit.counts[i],
    PIT: ipbox.pit.counts[i],
    Total: ipbox.cit.counts[i] + ipbox.pit.counts[i]
  }));
}

/**
 * Get 2022 reliefs comparison
 */
export function get2022ReliefsTimeSeries() {
  const { reliefs_2022 } = chartData;
  const years = reliefs_2022.prototyp.years;

  return years.map((year, i) => ({
    year,
    Robotyzacja: reliefs_2022.robotyzacja.cit.counts[i] + reliefs_2022.robotyzacja.pit.counts[i],
    Ekspansja: reliefs_2022.ekspansja.cit.counts[i] + reliefs_2022.ekspansja.pit.counts[i],
    CSR: reliefs_2022.csr.cit.counts[i] + reliefs_2022.csr.pit.counts[i],
    Prototyp: reliefs_2022.prototyp.cit.counts[i] + reliefs_2022.prototyp.pit.counts[i]
  }));
}

/**
 * Get average deduction per participant
 */
export function getAverageDeductionTimeSeries() {
  const { br } = chartData;
  return br.years.map((year, i) => {
    const totalCount = br.cit.counts[i] + br.pit.counts[i];
    const totalAmount = br.cit.amounts[i] + br.pit.amounts[i];
    return {
      year,
      average: totalCount > 0 ? (totalAmount / totalCount / 1000).toFixed(0) : 0 // in thousands PLN
    };
  });
}
