---
title: Blockchain Dashboard
theme: dashboard

---
```js
import * as Plot from "npm:@observablehq/plot";
const user_data = await FileAttachment("data/user_data.csv").csv({typed: true});
const transaction_data = await FileAttachment("data/transaction_data.csv").csv({typed: true});
const txn_user_data = await FileAttachment("data/txn_user_data.csv").csv({typed: true});
console.log(user_data)

const colorConfig = {
  domain: ['ethereum', 'base', 'optimism', 'arbitrum', 'polygon'],
  range: ['#D3D3D3','#28A0F0', '#FF0420', '#0052FF', '#9945FF']
};

const date_length = user_data.filter(d => d.blockchain === "ethereum").length;
console.log(date_length)
```

# Blockchain Transactions and Users 🔗

<div class="text-gray-500" style="width: 90%;">
This dashboard reports users and transaction data across Ethereum, Base, Optimism, Arbitrum, and Polygon since January 2025. 
</div>

Takeaways:
- Transactions have been trending down since January (20M -> 12M).
- Base has the highest number of transactions averaging around 9M per day, taking around 54% of transaction share</b>.
- Polygon has strong market presence with 20% of transaction share.
- Base has the highest number of active addresses averaging around 1M.
- Ethereum has a steady rate of ~3.5 transactions per day per user.
- L2s have more variability, ranging from around 6 to 12 daily txns per user.

<br>

## Daily Transactions   
<span class="text-sm text-gray-500"> Boxes show daily average transactions across ${date_length} days.</span>

<!-- Daily Transactions -->
<div class="grid grid-cols-3">
  <div class="card">
    <h2>Ethereum </h2>
    <span class="big">${(transaction_data.filter(d => d.blockchain === "ethereum").reduce((sum, d) => sum + d.transactions, 0) / date_length / 1000000).toLocaleString("en-US", {maximumFractionDigits: 2})}M</span>
  </div>
  <div class="card">
    <h2>Base </h2>
      <span class="big">${(transaction_data.filter(d => d.blockchain === "base").reduce((sum, d) => sum + d.transactions, 0) / date_length/ 1000000).toLocaleString("en-US", {maximumFractionDigits: 2})}M</span>
  </div>
  <div class="card">
    <h2>Optimism </h2>
      <span class="big">${(transaction_data.filter(d => d.blockchain === "optimism").reduce((sum, d) => sum + d.transactions, 0) / date_length/ 1000000).toLocaleString("en-US", {maximumFractionDigits: 2})}M</span>
  </div> 
  <div class="card">
    <h2>Arbitrum </h2>
    <span class="big">${(transaction_data.filter(d => d.blockchain === "arbitrum").reduce((sum, d) => sum + d.transactions, 0) / date_length/ 1000000).toLocaleString("en-US", {maximumFractionDigits: 2})}M</span>
  </div>
  <!-- <div class="card">
    <h2>Monad </h2>
    <span class="big">${(transaction_data.filter(d => d.blockchain === "monad").reduce((sum, d) => sum + d.transactions, 0) / date_length/ 1000000).toLocaleString("en-US", {maximumFractionDigits: 2})}M</span>
  </div> -->
  <div class="card">
    <h2>Polygon </h2>
    <span class="big">${(transaction_data.filter(d => d.blockchain === "polygon").reduce((sum, d) => sum + d.transactions, 0) / date_length/ 1000000).toLocaleString("en-US", {maximumFractionDigits: 2})}M</span>
  </div>
</div>

```js
function transactionTimeline(transaction_data, {width} = {}) {
  if (!transaction_data || transaction_data.length === 0) {
    console.error("No data available for plotting");
    return;
  }
 const validData = transaction_data.filter(d => d.date instanceof Date && !isNaN(d.date));

  return Plot.plot({
    title: "Daily Transactions",
    width: width || 1200,
    height: 300,
    y: {
      grid: true,
      label: "Transactions (Millions)",
      transform: d => d / 1000000,
      nice: true
    },
    x: {label: "Date", 
      type: "band",
    },
    color: {
      legend: true,
      domain: colorConfig.domain,
      range: colorConfig.range
    },
    marks: [
      Plot.rectY(validData, {
        x: "date",
        y: "transactions",
        fill: d => (d.blockchain || "").toLowerCase(),
        tip: {
          format: {
            y: (y) => (y).toLocaleString("en-US", {
              style: "decimal",
              maximumFractionDigits: 2
            }) + "M"
          }
        }
      }),
      Plot.ruleY([0])
    ]
  });
}
```

<div class="grid grid-cols-1">
  <div class="card">
    ${transactionTimeline(transaction_data, {width: 1200})}
  </div>
</div>


```js
import * as Highcharts from 'npm:highcharts';

function createPieChart(transaction_data) {
  // Calculate total transactions per blockchain
  const totals = transaction_data.reduce((acc, curr) => {
    if (!acc[curr.blockchain]) {
      acc[curr.blockchain] = 0;
    }
    acc[curr.blockchain] += curr.transactions;
    return acc;
  }, {});

  // Convert to array format needed for Highcharts
  const pieData = Object.entries(totals).map(([blockchain, value]) => ({
    name: blockchain.charAt(0).toUpperCase() + blockchain.slice(1),
    y: value,
    color: colorConfig.range[colorConfig.domain.indexOf(blockchain.toLowerCase())]
  }));

  const container = document.createElement('div');
  
  Highcharts.default.chart(container, {
    chart: {
      type: 'pie',
      width: width || 800,
      height: 400,
      style: {
        maxWidth: '100%',
      }
    },
    title: {
      text: 'Transaction Distribution (since January 2025)',
      style: {
        fontSize: '18px',
        fontWeight: 500,
        font: 'sans-serif'
      }
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          format: '{point.name}: {point.percentage:.1f}%',
          style: {
            fontSize: '12px',
            fontWeight: 300,
            font: 'sans-serif'
          }
        }
      }
    },
    series: [{
      name: 'Transactions',
      data: pieData
    }]
  });

  return container;
}
```

<div class="grid grid-cols-1">
  <div class="card">
    ${createPieChart(transaction_data)}
  </div>
</div>



## Daily Active Addresses  
<span class="text-sm text-gray-500"> Boxes show daily average active addresses across ${date_length} days.</span>

<!-- Daily Active Addresses -->
<div class="grid grid-cols-3">
  <div class="card">
    <h2>Ethereum </h2>
    <span class="big">${(user_data.filter(d => d.blockchain === "ethereum").reduce((sum, d) => sum + d.users, 0) / date_length/ 1000).toLocaleString("en-US", {maximumFractionDigits: 0})}K</span>
  </div>
  <div class="card">
    <h2>Base </h2>
    <span class="big">${(user_data.filter(d => d.blockchain === "base").reduce((sum, d) => sum + d.users, 0) / date_length/ 1000).toLocaleString("en-US", {maximumFractionDigits: 0})}K</span>
  </div>
  <div class="card">
    <h2>Optimism </h2>
      <span class="big">${(user_data.filter(d => d.blockchain === "optimism").reduce((sum, d) => sum + d.users, 0) / date_length/ 1000).toLocaleString("en-US", {maximumFractionDigits: 0})}K</span>
  </div> 
  <div class="card">
    <h2>Arbitrum </h2>
    <span class="big">${(user_data.filter(d => d.blockchain === "arbitrum").reduce((sum, d) => sum + d.users, 0) / date_length/ 1000).toLocaleString("en-US", {maximumFractionDigits: 0})}K</span>
  </div>
  <!-- <div class="card">
    <h2>Monad </h2>
    <span class="big">${(user_data.filter(d => d.blockchain === "monad").reduce((sum, d) => sum + d.users, 0) / date_length/ 1000).toLocaleString("en-US", {maximumFractionDigits: 0})}K</span>
  </div> -->
  <div class="card">
    <h2>Polygon </h2>
    <span class="big">${(user_data.filter(d => d.blockchain === "polygon").reduce((sum, d) => sum + d.users, 0) / date_length/ 1000).toLocaleString("en-US", {maximumFractionDigits: 0})}K</span>
  </div>
</div>

<br>

```js
function userTimeline(user_data) {
  if (!user_data || user_data.length === 0) {
    console.error("No data available for plotting");
    return;
  }
  return Plot.plot({
    title: "Daily Active Addresses",
    width: width || 1200,
    height: 300,
    y: {
      grid: true, 
      label: "Users (Thousands)",
      transform: d => d / 1000,
      nice: true
    },
    x: {label: "Date"},
    color: {
      legend: true,
      domain: colorConfig.domain,
      range: colorConfig.range
    },
    marks: [
      Plot.lineY(user_data, {
        x: "date",
        y: "users",
        stroke: d => (d.blockchain || "").toLowerCase(),
        strokeWidth: 1,
        tip: {
          format: {
            y: (y) => (y / 1000).toLocaleString("en-US", {
              style: "decimal",
              maximumFractionDigits: 2
            }) + "K"
          }
        }
      }),
      Plot.ruleY([0])
    ]
  });
}
```
<div class="grid grid-cols-1">
  <div class="card">
    ${userTimeline(user_data)}
  </div>
</div>


```js
function createUserPieChart(user_data) {
  // Calculate total users per blockchain
  const totals = user_data.reduce((acc, curr) => {
    if (!acc[curr.blockchain]) {
      acc[curr.blockchain] = 0;
    }
    acc[curr.blockchain] += curr.users;
    return acc;
  }, {});

  // Convert to array format needed for Highcharts
  const pieData = Object.entries(totals).map(([blockchain, value]) => ({
    name: blockchain.charAt(0).toUpperCase() + blockchain.slice(1),
    y: value,
    color: colorConfig.range[colorConfig.domain.indexOf(blockchain.toLowerCase())]
  }));

  const container = document.createElement('div');
  
  Highcharts.default.chart(container, {
    chart: {
      type: 'pie',
      width: width || 1200,
      height: 400
    },
    title: {
      text: 'User Distribution (since January 2025)',
      style: {
        fontSize: '18px',
        fontWeight: 500,
        font: 'sans-serif'
      }
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          format: '{point.name}: {point.percentage:.1f}%',
          style: {
            fontSize: '12px',
            fontWeight: 300,
            font: 'sans-serif'
          }
        }
      }
    },
    series: [{
      name: 'Users',
      data: pieData
    }]
  });

  return container;
}
```

<div class="grid grid-cols-1">
  <div class="card">
    ${createUserPieChart(user_data)}
  </div>
</div>


<br>

## Daily Transactions per Address  
<span class="text-sm text-gray-500"> Boxes show daily average transactions per user across ${date_length} days.</span>

<!-- Daily Transactions per User -->
<div class="grid grid-cols-3">
  <div class="card">
    <h2>Ethereum </h2>
    <span class="big">${(txn_user_data.filter(d => d.blockchain === "ethereum").reduce((sum, d) => sum + d.txn_per_user, 0) / date_length).toLocaleString("en-US", {maximumFractionDigits: 0})}</span>
  </div>
  <div class="card">
    <h2>Base </h2>
    <span class="big">${(txn_user_data.filter(d => d.blockchain === "base").reduce((sum, d) => sum + d.txn_per_user, 0) / date_length).toLocaleString("en-US", {maximumFractionDigits: 0})}</span>
  </div>
  <div class="card">
    <h2>Optimism </h2>
    <span class="big">${(txn_user_data.filter(d => d.blockchain === "optimism").reduce((sum, d) => sum + d.txn_per_user, 0) / date_length).toLocaleString("en-US", {maximumFractionDigits: 0})}</span>
  </div> 
  <div class="card">
    <h2>Arbitrum </h2>
    <span class="big">${(txn_user_data.filter(d => d.blockchain === "arbitrum").reduce((sum, d) => sum + d.txn_per_user, 0) / date_length).toLocaleString("en-US", {maximumFractionDigits: 0})}</span>
  </div>
  <div class="card">
    <h2>Polygon </h2>
    <span class="big">${(txn_user_data.filter(d => d.blockchain === "polygon").reduce((sum, d) => sum + d.txn_per_user, 0) / date_length).toLocaleString("en-US", {maximumFractionDigits: 0})}</span>
  </div>
</div>

```js
function txn_user_timeline(txn_user_data, {width} = {}) {
  if (!txn_user_data || txn_user_data.length === 0) {
    console.error("No data available for plotting");
    return;
  }
  return Plot.plot({
    title: "Daily Average Transactions per Address",
    width: width || 1200,
    height: 300,
    y: {
      grid: true, 
      label: "Transactions per Address",
      transform: d => d,
      nice: true
    },
    x: {label: "Date"},
    color: {
      legend: true,
      domain: colorConfig.domain,
      range: colorConfig.range
    },
    marks: [
      Plot.lineY(txn_user_data, {
        x: "date",
        y: "txn_per_user",
        stroke: d => (d.blockchain || "").toLowerCase(),
        strokeWidth: 1,
        tip: {
          format: {
            y: (y) => (y ).toLocaleString("en-US", {
              style: "decimal",
              maximumFractionDigits: 2
            })
          }
        }
      }),
      Plot.ruleY([0])
    ]
  });
}
```
<div class="grid grid-cols-1">
  <div class="card">
    ${txn_user_timeline(txn_user_data, {width: 1200})}
  </div>
</div>