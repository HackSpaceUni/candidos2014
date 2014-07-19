# Scrapy settings for jne project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jne'

SPIDER_MODULES = ['jne.spiders']
NEWSPIDER_MODULE = 'jne.spiders'

ITEM_PIPELINES = {
'jne.pipelines.JnePipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jne (+http://www.yourdomain.com)'
