plotFrequency <- function(data, cat, head_count, fill_color,horz){
  gg = data %>%
    filter_(!is.na(cat)) %>%
    count_(cat) %>%
    arrange(desc(n)) %>%
    mutate_(cat=reorder(cat,n)) %>%
    head(head_count) %>%
    
    ggplot(aes(x=cat,y=n)) +
    geom_bar(stat='identity', colour='white', fill=fill_color) +
    geom_text(aes(x=cat,y=1, label=paste0("(",n,")")),vjust=.5,hjust=0,colour='black',fontface='bold') +
    labs(x="cat",title="10 Most Popular cats",y="Count")+
    theme_bw()
    
    if(horz){
      gg = gg+coord_flip()
    }else{
      gg = gg+theme(axis.text.x = element_text(angle = 90, hjust = 1))
    }
}
