An attempt at coding up a visual odometry system to learn about computer vision.
Following multiple tutorials, but mostly inspired by [twitchslam](https://www.youtube.com/watch?v=7Hlb8YX2-W8&t=14738s) by George Hotz.
Check out the accompanying series of blog posts [here](https://vibhavgaur.github.io/visodo-1.html)

I attempted to bookmark some points in the twitchslam streams for my reference during my multiple viewings -- you may find it helpful too. 
I will post this on as a YouTube comment once I make my way through the stream(s).

### twitchslam | Part 1

| Commit name | Timestamp |
| ----------- | --------- |
| feature extractor | 1:30:00 |
| normalized coords | 1:55:17 |
| Essential matrix pose recovery | 2:29:28 |
| Built g2o for MacOSX | 3:31:57 |
| Refactor to Frame class | 3:57:00 |

#### Points of importance

| Description | Timestamp |
| ----------- | --------- |
| Chose 200 as focal length "because we tried a bunch of numbers and it worked" | 2:03:02 |
| Extracted camera pose from Essential Matrix -- a visual odometry system | 2:23:00 |
