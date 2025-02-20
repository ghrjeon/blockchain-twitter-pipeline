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
  domain: ['ethereum', 'base', 'optimism', 'arbitrum'],
  range: ['#9945FF','#28A0F0', '#FF0420', '#0052FF', ]
};

const date_length = user_data.filter(d => d.blockchain === "ethereum").length;
console.log(date_length)
```

# Blockchain Transactions and Users 🔗

<div class="text-gray-500" style="width: 90%;">
This dashboard reports users and transaction data across <b>Ethereum, Base, Optimism, and Arbitrum</b> since January 2025. 
</div>

<p style="font-size: 11px; width: 95%;"> 
* Please note that the purpose of this dashboard is to demonstrate analytical engineering capabilities using independent DS/DE tools. Check out an example of a more comprehensive dashboarding for data insights using existing platforms here: <a href="https://dune.com/theano2247/me-and-tensor-market-analysis">https://dune.com/theano2247/me-and-tensor-market-analysis</a>. 
</p>


Takeaways:
- Ecosystem transactions have been trending down since January, from aournd 15M to 12M total transactions.
- Base has the highest number of daily transactions averaging around 9M, as well as active addresses averaging around 1M.
- Ethereum has a steady transactions per user while other ecosystems have more variability in numbers, ranging from around 6 to 12 txns per user.
- Optimism has the highest number of transactions per address.



<br>

## Daily Transactions   
<span class="text-sm text-gray-500"> Boxes show daily average transactions across ${date_length} days.</span>

<!-- Daily Transactions -->
<div class="grid grid-cols-2">
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
            y: (y) => (y / 1000000).toLocaleString("en-US", {
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

<br>

## Daily Active Addresses  
<span class="text-sm text-gray-500"> Boxes show daily average active addresses across ${date_length} days.</span>

<!-- Daily Active Addresses -->
<div class="grid grid-cols-2">
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
</div>

<br>

```js
function userTimeline(user_data, {width} = {}) {
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
        strokeWidth: 2,
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
    ${userTimeline(user_data, {width: 1200})}
  </div>
</div>


<br>

## Daily Transactions per Address  
<span class="text-sm text-gray-500"> Boxes show daily average transactions per user across ${date_length} days.</span>

<!-- Daily Transactions per User -->
<div class="grid grid-cols-2">
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
        strokeWidth: 2,
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