try:
    import os
    import argparse
    from FilmScraper import filmScraper 
    import FilmScraper
    from config import Config
except Exception as e:
    print("Caught exception while importing: {}".format(e))
    
if __name__ == '__main__':
    parser= argparse.ArgumentParser(description="")
    parser.add_argument('--dir', help='output dir', default='Output', type=str)
    parser.add_argument('--file', help='output file', default='image_data', type=str)
    parser.add_argument('-st', '--start', help="the start page for search", default=1, type=int)
    parser.add_argument('-np', '--number-of-pages', help='number of pages for search', default=5, type=int )
    args = parser.parse_args()
    print("Start crawling...")
    print(args)
    
    current_path = os.getcwd()
    save_dir = current_path + '/' + args.dir
    
    configs = Config(save_dir= save_dir, save_file= args.file,start=args.start, number=args.number_of_pages)
    crawler = filmScraper(configs)
    crawler.film_crawler