class MoviesLocators:
    FILTER_GENRE = "[data-qa-id='movies_filter_genre_select']"         # фильтр «Жанр»
    FILTER_LOCATION = "[data-qa-id='movies_filter_location_select']"  # триггер «Место»
    FILTER_CREATED_AT = "[data-qa-id='movies_filter_created_at_select']"  # сортировка
    LOCATION_OPTION_MSK = "[role='option']:has-text('MSK')"  # опция «MSK» в списке
    MORE_BUTTON = "[data-qa-id='more_button']"      # «Подробнее» (у каждой карточки)
    CARD_TITLE = "h3"  # заголовок карточки фильма