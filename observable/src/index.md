---
toc: false
theme: dashboard
---

<div class="hero">
  <h1>Welcome to Rosalyn's Blockchain and Twitter Analytics Dashboard!</h1>
</div>

<div class="content">
<h3> Content </h3>
📌 Keywords Dashboard: Reports daily keywords in crypto twitter across the ecosystem. <br>
📌 Tweets Dashboard: Provides a list of top tweets with high attention. <br>
<!-- 📌 Blockchain Dashboard: Reports users and transaction data across blockchain ecosystems. <br> -->
</div> 
<br>

<div class="content">
<h3> Stacks used in this project </h3>
- Data Lake/Warehouse: BigQuery, Google Cloud Buckets <br>
- Data Modeling: DTB, Python <br>
- Data Visualization: Observable.js, D3.js  <br>
- APIs: SocialData, OpenAI <br>
<!-- - APIs: Flipside Crypto, SocialData, OpenAI <br> -->
</div>
<br>
<div class="content">
<h3>Next steps:  </h3>
- Convert the pipeline into incremental ingestion. <br>
- Automate dag using GitHub Actions workflow or Airflow. <br>
<br>

<div class="grid grid-cols-2">
  <div class="card">
    <a href="https://github.com/ghrjeon/blockchain-twitter-pipeline"><code> Github to this project</code><span style="display: inline-block; margin-left: 0.25rem;">↗︎</span></a>
  </div>
  <div class="card">
    <a href="https://www.linkedin.com/in/ghrjeon"><code> Rosalyn's Linkedin</code><span style="display: inline-block; margin-left: 0.25rem;">↗︎</span></a>
  </div>
    <div class="card">
    <a href="https://dune.com/theano2247/me-and-tensor-market-analysis"><code> Rosalyn's Dune Dashboard</code><span style="display: inline-block; margin-left: 0.25rem;">↗︎</span></a>
  </div>
</div>


<style>

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 1rem 0 1rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 1rem 0;
  padding: 1rem 0;
  max-width: none;
  font-size: 30px;
  font-weight: 400;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.content {
  color:rgb(12, 31, 50);
  line-height: 1.6;
  font-size: 1.1rem;
}



</style>
