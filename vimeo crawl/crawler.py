import urllib2, urllister
import MySQLdb.cursors
tocrawl = set(["http://vimeo.com/jaugustavo"])
crawled = set([])
vimeo="http://vimeo.com"
k=0
while k<=5000:
    try:
        crawling = tocrawl.pop()
    except KeyError:
        raise StopIteration
    k=k+1
    pay='NO'
    Staffpick='NO'
    Video='NO'
    try:
        usock = urllib2.urlopen(crawling)
        msg = usock.read()
        conn = MySQLdb.connect(host='',user='root', passwd='vishal', db='vimeo')
        cursor = conn.cursor ()
        sql="""INSERT INTO user_info(Name,URL,Paying,StaffPick,Video) VALUES (%s,%s,%s,%s,%s)"""
        if msg.find('data-ga-event="button|plus_badge_click|plus"')!=-1:
            pay='YES'
        if msg.find('featured_videos')!=-1:
            Staffpick='YES'
        if msg.find('recent_videos')!=-1:
            Video='YES'
        start=msg.find('title=')
        end=msg.find('Videos',start+7)
        name=msg[start+7:end-9]
        print name
        query_args = [name,crawling,pay,Staffpick,Video]
        cursor.execute (sql,query_args)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as ex:
        print ex
    startPos = msg.find('<ul class="profile_following">')
    if startPos != -1:
        endPos = msg.find('</ul>',startPos+3)
        if endPos != -1:
            title = msg[startPos+3:endPos]
            parser = urllister.URLlister()
            parser.feed(title)
            usock.close()
            parser.close()
            for url in parser.urls:
                if(vimeo+url not in crawled):
                    tocrawl.add(vimeo+url)
                    crawled.add(vimeo+url)
                    print len(crawled)