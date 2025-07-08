# Variable Dictionary: Cleaned Spotify Songs 2024

This document describes the variables in the **cleaned** dataset (`cleaned_spotify_data_2024.csv`). All column names are standardized to `lowercase_with_underscores`.

| Variable Name                | Data Type | Unit / Format | Description                                                                                          |
| ---------------------------- | --------- | ------------- | ---------------------------------------------------------------------------------------------------- |
| `track`                      | `string`  | -             | The official name of the song track.                                                                 |
| `album_name`                 | `string`  | -             | The name of the album or single the track belongs to.                                                |
| `artist`                     | `string`  | -             | The name of the primary artist credited on the track.                                                |
| `release_date`               | `datetime`| YYYY-MM-DD    | The date when the track was released.                                                                |
| `isrc`                       | `string`  | ID            | International Standard Recording Code, a unique identifier for the specific recording.               |
| `all_time_rank`              | `string`  | Rank          | The track's all-time rank on Spotify. May contain non-numeric values.                                |
| `track_score`                | `float`   | Score         | An internal score representing the track's overall performance.                                      |
| `spotify_streams`            | `int64`   | Count         | Total streams on Spotify. **This is our primary target variable.** |
| `spotify_playlist_count`     | `float64` | Count         | Number of public Spotify playlists the track is a part of.                                           |
| `spotify_playlist_reach`     | `float64` | Count         | Total followers across all Spotify playlists the track is on.                                        |
| `spotify_popularity`         | `float64` | 0-100         | A score (0-100) representing the track's current popularity on Spotify.                              |
| `youtube_views`              | `float64` | Count         | Total views of the track's official video on YouTube.                                                |
| `youtube_likes`              | `float64` | Count         | Total likes of the track's official video on YouTube.                                                |
| `tiktok_posts`               | `float64` | Count         | Number of TikTok posts using this track.                                                             |
| `tiktok_likes`               | `float64` | Count         | Total likes across all TikTok posts using this track.                                                |
| `tiktok_views`               | `float64` | Count         | Total views across all TikTok posts using this track.                                                |
| `Youtubelist_reach`     | `float64` | Count         | Total subscribers across all YouTube playlists the track is on.                                      |
| `apple_music_playlist_count` | `float64` | Count         | Number of public Apple Music playlists the track is a part of.                                       |
| `airplay_spins`              | `float64` | Count         | Number of times played on radio, as tracked by AirPlay.                                              |
| `siriusxm_spins`             | `float64` | Count         | Number of times played on SiriusXM satellite radio.                                                  |
| `deezer_playlist_count`      | `float64` | Count         | Number of public Deezer playlists the track is a part of.                                            |
| `deezer_playlist_reach`      | `float64` | Count         | Total followers across all Deezer playlists the track is on.                                         |
| `amazon_playlist_count`      | `float64` | Count         | Number of public Amazon Music playlists the track is a part of.                                      |
| `pandora_streams`            | `float64` | Count         | Total streams on Pandora.                                                                            |
| `pandora_track_stations`     | `float64` | Count         | Number of user-created stations on Pandora based on this track.                                      |
| `soundcloud_streams`         | `float64` | Count         | Total streams on Soundcloud.                                                                         |
| `shazam_counts`              | `float64` | Count         | Total times the track has been identified using Shazam.                                              |
| `tidal_popularity`           | `float64` | 0-100         | A score representing the track's popularity on TIDAL.                                                |
| `explicit_track`             | `int64`   | 0 or 1        | A flag indicating if the track is explicit (1 for True, 0 for False).                                |