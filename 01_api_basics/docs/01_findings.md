# Findings

## Missing GitHub information

While exporting data from the first five protocols returned by the DeFiLlama API, most of the `github` fields had a `null` value.

The first results included Binance CEX, OKX, Bitfinex, Lido and Bybit. Four of these are centralised exchanges, while Lido is a decentralised protocol.

Lido included a GitHub organisation:

```json
"github": [
    "lidofinance"
]
```

The centralised exchanges returned:

```json
"github": null
```

### Possible explanation

Centralised exchanges normally do not publish the source code of their main platforms. Decentralised protocols are more likely to publish their smart contracts and development repositories.

### Possible improvement

Future versions of the script could:

* Filter out centralised exchanges.
* Select protocols by category.
* Select only protocols with available GitHub information.
* Record missing values explicitly.
