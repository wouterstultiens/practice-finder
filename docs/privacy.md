# Privacy Policy

**Vacancy Monitor**  
GitHub: https://github.com/wouter-stultiens/practice-finder

**Last updated: 2025-06-06**

## 1. Introduction

Practice Finder is a small tool that periodically fetches **public** Facebook page posts and publicly accessible vacancy pages.  
It does not collect any personal data (names, emails, or user-specific identifiers). All the Facebook data it reads is public page content.

## 2. What data we access

- **Facebook page posts** (public posts only).  
- **Job listings** on public websites (vacaturepagina’s) for dental practices.

We **never** scrape private profiles or user comments. We do not store any user’s personal information.

## 3. How we use that data

1. **Fetch & detect new vacancy posts.**  
   We fetch the latest N posts from configured Facebook Pages.  
2. **Analyze with a language model.**  
   We send only the **public post text** to an LLM for vacancy extraction and summarization (no user metadata).  
3. **Send summary notifications.**  
   If a vacancy is detected, we send a brief summary to a Telegram chat.  
4. **State tracking.**  
   We store only the “last seen timestamp” for each page to avoid reprocessing the same posts.

## 4. No personal data storage

- We **never** record or store any user’s private information, IP addresses, or cookies.  
- We do store (in Google Cloud Storage) only:
  - The last‐seen HTML snapshot of each public vacancy page (for diffing).  
  - The last‐seen timestamp for each Facebook page (to avoid reprocessing).  
- All stored snapshots are tied to **page URLs** or **page IDs**, not to individual users.

## 5. Cookies & tracking

Vacancy Monitor itself does not use cookies. If you visit the Facebook website or Telegram, they may place cookies in your browser—but that is outside this project’s scope.

## 6. Contact

If you have any questions about this Privacy Policy, please contact:  
