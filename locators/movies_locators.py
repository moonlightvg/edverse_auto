class MoviesLocators:
    FILTER_LOCATION = "[data-qa-id='movies_filter_location_select']"  # триггер «Место»
    LOCATION_OPTION_MSK = "[role='option']:has-text('MSK')"  # опция «MSK» в списке
    CARD_TITLE = "h3"  # заголовок карточки фильма