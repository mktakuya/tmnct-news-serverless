require "fileutils"

require "sequel"

def transform(news:)
  {
    title: news[:title],
    wp_pid: news[:wp_pid],
    url: news[:url],
    pub_date: news[:pub_date].iso8601,
    category: news[:name],
    content: news[:content],
    slug: news[:slug],
  }
end

if $0 == __FILE__
  database_url = ENV.fetch("DATABASE_URL")
  raise "DATABASE_URL is not set" if database_url.empty?

  print "Connecting to database..."
  DB = Sequel.connect(database_url)
  puts " done."

  print "Fetching all news..."
  all_news = DB[:news].join(:categories, id: :category_id).all
  puts " done."

  print  "Erasing output/ dir..."
  FileUtils.rm_rf("output/*")
  puts " done."

  print "Exporting news..."
  all_news.each do |news_raw|
    news = transform(news: news_raw)
    file_name = "#{news[:wp_pid]}.json"

    File.write("output/#{file_name}", news.to_json)
  end
  puts " done."
end
