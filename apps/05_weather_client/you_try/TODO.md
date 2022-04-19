# Implementation Plan

## Branches
- Asyncio
- Worker
- Twisted
- Celery

### Components
- REPL prompt
- Wunderground API client
- Markup Scraper(bs4)
- Message queue (amqp)

### Tasks
- Parse inputs
  - Validate format
  - Prepare payload
  - Send payload to wunderground client
- Send wunderground forecast request
  - GET response
  - Send response to Markup Scraper
- Markup Scraper parses response payload
  - Scraper extracts values from relevant elements
  - Scraper sends values to response output
- Response output is printed to stdout/printline  