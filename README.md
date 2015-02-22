# Why?

I got some issues with Telstra & TPG - their line quality is pretty
bad for me in these days. The noise level on my landline is way too
high, and this results bad connections (extremely slow). To check if
there is a pattern, I need to scrape the stats from my modem.

I guess I can surely retrieve this information using SNMP, but that's
too hard-core sysadmin work for me.


# Structure

`stats.py` retrieve and parse ADSL stats, and publish it to
datadog. ADSL RX realtime data can be seen on
[datadog](https://app.datadoghq.com/graph/embed?from_ts=1424426746869&to_ts=1424599546869&token=79a1773c617b0b6f59a54a841066fb6772ce05cabbb1bb32cd607588fcbe5cc5&height=400&width=800&legend=true&tile_size=m&live=true).


# Screenshot

![datadog](datadog_result.png?raw=true "Datadog screenshot")

