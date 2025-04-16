---
theme: dashboard
title: Keywords Dashboard
toc: false
---
```js
import * as Plot from "npm:@observablehq/plot";
const keywords_data = await FileAttachment("data/keywords_data.csv").csv({typed: true});

const bitcoin_data = Array.from(keywords_data).filter(row => row.ecosystem === "bitcoin");
const ethereum_data = Array.from(keywords_data).filter(row => row.ecosystem === "ethereum");
const solana_data = Array.from(keywords_data).filter(row => row.ecosystem === "solana");
const nft_data  = Array.from(keywords_data).filter(row => row.ecosystem === "nft");
const defi_data = Array.from(keywords_data).filter(row => row.ecosystem === "defi");
const depin_data = Array.from(keywords_data).filter(row => row.ecosystem === "depin");

console.log(keywords_data)
```

# Blockchain Ecosystem Twitter Keywords 🔗 

<div class="text-gray-500" style="width: 80%;">
This dashboard provides insights into the most discussed topics across blockchain ecosystems, highlighting daily key trends and words. It offers a quick and comprehensive overview of the ecosystem, enabling users to stay informed at a glance.
</div>
<br>

### Methodology

<div class="text-gray-500" style="width: 80%;">
I collect tweets that mention each blockchain ecosystem, filtering for those with significant engagement. LLM is applied to extract and summarize the key topics of discussion for each day. Please see <a href="https://github.com/ghrjeon/blockchain-twitter-pipeline">Github</a> for details on filter configurations and the prompts used.
</div>

<br>
<style>
  .observablehq--table .observablehq--index-column,
  .observablehq--table tbody tr td:first-child,
  .observablehq--table thead tr th:first-child {
    display: none !important;
  }
</style>

## Bitcoin
```js
const bitcoin_table = Inputs.table(bitcoin_data, {
  width: {
    date: "15%",
    ecosystem: "15%",
    keywords: "70%",
  },
  format: {
    keywords: d => htl.html`<span style="white-space:normal">${d}`
  },
  height: 300,
});
display(bitcoin_table);
```
## Ethereum
```js
const ethereum_table = Inputs.table(ethereum_data, {
  width: {
    date: "15%",
    ecosystem: "15%",
    keywords: "70%"
  },
  format: {
    keywords: d => htl.html`<span style="white-space:normal">${d}`
  },
  height: 300
});
display(ethereum_table);
```

## Solana    
```js
const solana_table = Inputs.table(solana_data, {
  width: {
    date: "15%",
    ecosystem: "15%",
    keywords: "70%"
  },
  format: {
    keywords: d => htl.html`<span style="white-space:normal">${d}`
  },
  height: 300
});
display(solana_table);
```

## DeFi
```js
const defi_table = Inputs.table(defi_data, {
  width: {
    date: "15%",
    ecosystem: "15%",
    keywords: "70%"
  },
  format: {
    keywords: d => htl.html`<span style="white-space:normal">${d}`
  },
  height: 300
});
display(defi_table);
```
## NFT
```js
const nft_table = Inputs.table(nft_data, {
  width: {
    date: "15%",
    ecosystem: "15%",
    keywords: "70%"
  },
  format: {
    keywords: d => htl.html`<span style="white-space:normal">${d}`
  },
  height: 300,
});
display(nft_table);
```

## Depin
```js
const depin_table = Inputs.table(depin_data, {
  width: {
    date: "15%",
    ecosystem: "15%",
    keywords: "70%"
  },
  format: {
    keywords: d => htl.html`<span style="white-space:normal">${d}`
  },
  height: 300
});
display(depin_table);
```
