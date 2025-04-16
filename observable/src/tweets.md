---
theme: dashboard
title: Tweets Dashboard
toc: false
---
```js
import * as Plot from "npm:@observablehq/plot";
import {csvParse, dsvFormat, csvFormat} from "d3-dsv";

const response = await fetch('https://api.allorigins.win/raw?url=' + 
  encodeURIComponent('https://storage.googleapis.com/blockchain_proto/top_tweets_000000000000.csv'));
if (!response.ok) throw new Error(`fetch failed: ${response.status}`);
const text = await response.text();
const columnMap = {
  'id': 'id',
  'date': 'date',
  'text': 'text',
  'user_screen_name': 'username',
  'retweet_count': 'retweets',
  'favorite_count': 'likes',
  'bookmark_count': 'bookmarks'
};
const parser = dsvFormat(";");
const tweets_data = parser.parse(text, d => ({
  ...Object.fromEntries(
    Object.entries(d).map(([key, value]) => [
      columnMap[key] || key,  // Use mapped name if exists, otherwise keep original
      key === 'date' ? new Date(value) :
      key === 'id' ? String(value) :  
      key === 'retweet_count' || key === 'favorite_count' || key === 'bookmark_count' ? +value :  
      value  
    ])
  )
}));
console.log(tweets_data)

// const tweets_data = await FileAttachment("data/twitter_data.csv").csv({typed: true});
const formatted_data = tweets_data
  .filter((tweet, index, self) => 
    index === self.findIndex(t => t.id === tweet.id)
  )
console.log(formatted_data)
```

# Blockchain Ecosystem Notable Tweets 🔗

<div class="text-gray-500" style="width: 90%;">
This dashboard provides access to notable tweets collected in the past week across blockchain ecosystems. It highlights tweets with significant attention and engagement, based on likes, bookmarks, and retweets. 
<br>
<div style="font-size: 13px; width: 95%;">
** it takes a few seconds to load! **
<br>
</div>

```js
const tweets_table = Inputs.table(formatted_data, {
      columns: [
        "date",
        "id",
        "text",
        "username",
        "likes",
        "bookmarks",
        "retweets",
        "ecosystem"
      ],
    width: {
    id: "15%",
    text: "30%"
  },
  format: {
    id: (value) => {
      const row = formatted_data.find(row => row.id === value);
      return htl.html`<a href="https://twitter.com/${row.username}/status/${String(value)}" target="_blank">${String(value)}</a>`
    },
    text: d => htl.html`<span style="white-space:normal">${(d || '').slice(0, 50)}...</span>`
  },
  height: 600,
  rows: 100 // Set specific height in pixels
});
display(tweets_table);
```