import scrape as gs
import pandas as pd

path = "/Users/richa/CDAC/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15, True, path, 15)


