import feedparser

#dados = feedparser.parse("https://vagas.sc/?feed=job_feed&job_types=efetivo%2Cn-i&search_location&job_categories&search_keywords")
dados = feedparser.parse("https://vagas.sc/?feed=job_feed&job_types=efetivo%2Cn-i&search_location&job_categories&search_keywords")
n = 0
for post in dados['entries']:
    print('*' * 30)
    print(n)
    n += 1
    print(f'=>> title:  {post["title"]}')
#    print(f'=>> title_detail: {post["title_detail"]}')
#    print(f'=>> links: {post["links"]}')
#    print(f'=>> link: {post["link"]}')
#    print(f'=>> authors: {post["authors"]}')
#    print(f'=>> author: {post["author"]}')
#    print(f'=>> published: {post["published"]}')
#    print(f'=>> published_parsed: {post["published_parsed"]}')
#    print(f'=>> id: {post["id"]}')
#    print(f'=>> guidislink: {post["guidislink"]}')
#    print(f'=>> summary: {post["summary"]}')
#    print(f'=>> summary_detail: {post["summary_detail"]}')
#    print(f'=>> content: {post["content"]}')
#    print(f'=>> job_listing_location: {post["job_listing_location"]}')
#    print(f'=>> job_listing_job_type: {post["job_listing_job_type"]}')
#    print(f'=>> job_listing_company: {post["job_listing_company"]}')
    print('*' * 30)
#    print(post)
    print('*' * 30)
