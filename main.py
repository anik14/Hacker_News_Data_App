

#python main to work with the apps and database
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        self.response.out.write("""
          <html>
            <body>
              <form action="/storyCount" method="post">
                <div><p>A. How many stories in Hacker News?</p></div>
                <div><a href="http://localhost:8080/storyCount">Number of news</a></div>
              </form>
            </body>
          </html>

          <html>
            <body>
              <form action="/score" method="post">
                <div><p>B. Which story have the lowest score?</p></div>
                <div><a href="http://localhost:8080/score">Lowest score</a></div>
                <div><a href="https://datastudio.google.com/open/0B0J2JkD2fP9tZkpVYzUwcDdERkk">Scatter Chart</a></div>
              </form>
            </body>
          </html>
          
          <html>
            <body>
              <form action="/scoreAvg" method="post">
                <div><p>C. Best url story in 2015?</p></div>
                <div><a href="http://localhost:8080/scoreAvg">Top 5 of Hacker News</a></div>
                <div><a href="https://datastudio.google.com/open/0B0J2JkD2fP9tQ3p1cUh3RlB6cnc">Line chart</a></div>
              </form>
            </body>
          </html>

          <html>
            <body>
              <form action="/storyList" method="post">
                <div><p>D. Author in blogspot.com and yahoo.com?</p></div>
                <div><a href="http://localhost:8080/storyList">Author in blogspot and yahoo</a></div>
                <div><a href="https://datastudio.google.com/open/0B0J2JkD2fP9tNEMtdkN2eXBTelk">Report</a></div>
             </form>
            </body>
          </html>




          """)

#call the classes
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/storyCount', 'hacker_news_query.StoryCount'),
    ('/score', 'scoreLowest.Score'),
    ('/scoreAvg','url_avg.scoreAvg'),
    ('/storyList', 'story_list.storyList'),
    ('/domainAvg', 'domain_avg_2015.domainAvg')
], debug=True)
