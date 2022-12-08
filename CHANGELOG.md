# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2022-11-22
### Added
### Changed
 - SDAP-408: Improve L2 satellite data ingestion speed
   - Improved fault tolerance of writes to data & metadata stores. For ingestion pipelines that generate many tiles, the data stores may fail on some writes which was treated as an unrecoverable failure. Now more tolerant of this.
   - Batched writes: Reduced the number of network IO operations by consolidating writes of tile data + metadata.
   - Removed unnecessary function call. Removed an unneeded function call that seemed to be consuming a lot of pipeline runtime.
   - Batched tasks submitted to executors in pool. Saves wasted time switching between completed & new tasks.
### Deprecated
### Removed
### Fixed
### Security


