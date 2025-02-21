---
toc: false
theme: dashboard
---

<div class="hero">
  <h1>Welcome to Rosalyn's Blockchain and Twitter Analytics Dashboard!</h1>

  <div class="text-gray-500" style="width: 92%;">
  The goal of this project is to demonstrate my analytical engineering skills, domain knowledge in Blockchain, 
  and ability to incorporate AI tools in data analysis. 
  I am a PhD candidate in Economics looking for a role where I can apply these skills and build with a team!
  </div>
</div>
<br>

### Stacks used in this project
- Data Warehousing: BigQuery, Google Cloud Buckets
- Data Modeling: DTB, Python
- Data Visualization: Observabl.js, D3.js 
- APIs: Flipside Crypto, SocialData, OpenAI

Next steps: 
- Convert the pipeline into incremental ingestion. 
- Automate dag using GitHub Actions workflow or Airflow. 

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

.hero h2 {
  margin: 0;
  max-width: 50%;
  font-size: 20px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--theme-foreground-muted);
}



</style>
