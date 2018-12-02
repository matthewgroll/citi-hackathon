library(pdftools)

a <- pdf_text('/Users/charleschen/Desktop/citi hackathon/Resume&Job_Backup/Original_Resumes/1Amy.pdf')

pdf_split_word <- function(a){
  a <- paste(a, collapse = ' ')
  a_split <- strsplit(a, split = '\\s|\\n|\\t|[[:punct:]]+')
  b <- c()
  for (i in 1:length(a_split[[1]])){
    if (identical(a_split[[1]][i], "") == FALSE){
      b <- c(b, a_split[[1]][i])
    }
  }
  b 
}

# extrat key words
b <- pdf_split_word(a)
for (i in 1:length(pos_preposition)){
  regmatches(a, gregexpr(pos_preposition[1],a))[[1]]
}
regmatches(b, gregexpr(pos_preposition[31],b))
b <- b[c(b %in% pos_preposition == FALSE)]
b <- b[c(b %in% sw_mallet == FALSE)]
b <- b[-grep("[0-9]+", b)]
month <- c('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Sept', 
           'Oct', 'Nov', 'Dec')
b <- b[c(b %in% sw_mallet == FALSE)]