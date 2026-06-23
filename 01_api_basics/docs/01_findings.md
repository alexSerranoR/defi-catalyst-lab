## Missing GitHub data and centralised exchanges

### Problem

The first version of the script selected the first five protocols returned by the DeFiLlama API.

Several of these projects were centralised exchanges, such as Binance, OKX, Bitfinex and Bybit. Most of them returned a `null` value in the `github` field.

This was not a Python error. It indicated that DeFiLlama did not provide GitHub information for those projects through the protocol endpoint.

A second issue was discovered after filtering only by GitHub availability: projects categorised as centralised exchanges could still appear if they had a registered GitHub organisation. Robinhood was an example of this situation.

### Solution

The script was updated to apply two filters:

1. Protocols without GitHub information are skipped.
2. Protocols whose category is `CEX` are skipped.

The program continues checking projects until five protocols that satisfy both conditions have been collected.

The category filter is applied before requesting the complete protocol information whenever possible. This avoids unnecessary API requests and improves execution time.

### Result

The generated JSON dataset now contains five non-CEX protocols with available GitHub information.

This produces a dataset that is more relevant for analysing open-source DeFi projects. However, GitHub availability alone should not be considered proof that a project is decentralised. Additional indicators, such as governance, smart-contract architecture and contributor activity, may be required in future analyses.
