
library(XML)
library(RCurl)
library(rlist)

tables <- readHTMLTable(theurl)
tables <- list.clean(tables, fun = is.null, recursive = FALSE)
n.rows <- unlist(lapply(tables, function(t) dim(t)[1]))

observations <- htmltab(doc = theurl, which = "//th[text() = 'Date/ Time (CDT)']/ancestor::table")
