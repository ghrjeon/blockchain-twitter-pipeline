import {csvFormat} from "d3-dsv";

// Fetch the API data
const response = await fetch('https://api.allorigins.win/raw?url=' + 
  encodeURIComponent('https://storage.googleapis.com/blockchain_proto/daily_users_000000000000.csv'));
if (!response.ok) throw new Error(`fetch failed: ${response.status}`);
const text = await response.text();

// Parse the CSV data
const data = text.split('\n')
  .map(row => row.split(','))
  .slice(1) // Skip header row
  .map(([date, users, blockchain]) => ({
    date: new Date(date),
    users: Number(users),
    blockchain: blockchain
  }));

process.stdout.write(csvFormat(data));
