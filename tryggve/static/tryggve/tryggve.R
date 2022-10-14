library(mapproj)
library(tidyverse)
library(countrycode)
library(googledrive)
library(scales)

my_theme <- 
  theme(
    # remove  the default ggplot gridlines and grey background
    panel.grid = element_blank(),
    panel.background = element_rect(fill = "#ffffff"),
    
    # remove X and Y AXIS
    axis.text = element_blank(),
    axis.ticks = element_blank(),
    axis.title = element_blank(),
    
    # Not sure what exactly this does?
    plot.margin = unit(c(0, 0, 0.5, 0), 'cm'),
    
    # Set  the position of the prevalence legend at the bottom, and increase its width.
    legend.position="none", legend.key.width = unit(1.3, 'cm') 
  ) 


# Get dataset of lat + longitdude for countries via mapproj package
tbl <- map_data("world") %>% 
  filter(region != "Antarctica") %>% tibble() %>% 
  mutate(iso3c = countrycode(sourcevar = region, origin = "country.name", destination = "iso3c"))

# mapplot_world <- 
#   ggplot() + 
#   geom_map(data=tbl, map=tbl, 
#            aes(long, lat, map_id=region), 
#            colour="grey", size=0.1) +
#   coord_map("rectangular", lat0=0, xlim=c(-180,180), ylim=c(-60, 90))


dat <- tbl %>% 
  filter(long > -10 & long <= 40, lat > 37 & lat <= 75) %>% 
  mutate(tryggve = if_else(region %in% c("Norway", "Sweden", "Denmark", "Estonia"), 1,0)) %>% 
  filter(!region %in% c("Russia", "Turkey", "Greece", "Spain", "Portugal", "Algeria", "Italy"))



ggplot() + 
  geom_map(data=dat, map=dat, 
           aes(long, lat, map_id=region, fill = tryggve), 
           colour="grey", size=0.1) +
  coord_map("gall", lat0=0) +
  scale_fill_gradient(labels = percent) +
  my_theme

ggsave("/Users/arvhar/projects/tryggve_webpage/tryggve/static/tryggve/tryggve_map.png")