workspace "Электронная почта" {
    name "Система электронной почты"

    model {
        user = person "Пользователь" {
            description "Человек, который отправляет и получает письма"
        }

        // C2
        email_system = softwareSystem "Электронная почта" {
            description "Позволяет работать с почтовыми папками, сообщениями и пользователями"

            // C2
            database = container "База данных" {
                description "Хранит данные о письмах, пользователях и папках"
                technology "PostgreSQL"
            }

            // C2
            api_server = container "Серверный API" {
                description "Обрабатывает запросы пользователей, управляет пользователями, папками и письмами"
                technology "Python FastAPI"
                -> database "Читает и сохраняет данные"

                // C3
                user_management = component "Управление пользователями" {
                    description "Реализует управление данными пользователей (создание, поиск)"
                    technology "Python FastAPI"
                }

                folder_management = component "Управление папками" {
                    description "Реализует управление почтовыми папками (создание, получение списка)"
                    technology "Python FastAPI"
                }

                email_management = component "Управление письмами" {
                    description "Реализует создание, получение и поиск писем"
                    technology "Python FastAPI"
                }

                api_router = component "REST API маршрутизация" {
                    description "Обрабатывает маршруты и распределяет запросы между компонентами"
                    technology "Python FastAPI"
                }

                api_router -> user_management "Передает запросы, связанные с пользователями"
                api_router -> folder_management "Передает запросы, связанные с папками"
                api_router -> email_management "Передает запросы, связанные с письмами"
            }

            web_app = container "Веб-приложение" {
                description "Приложение для взаимодействия с системой электронной почты через браузер"
                technology "React, REST API"
                -> api_server "Делает API запросы"
            }

            // С2
            user -> email_system "Взаимодействует с системой электронной почты"

            // С2
            user -> web_app "Взаимодействует с веб-интерфейсом"

            // С3
            user_management -> database "Читает и записывает данные пользователей"
            folder_management -> database "Читает и записывает данные папок"
            email_management -> database "Читает и записывает данные писем"
        }
    }

    views {
        themes default

        // C1
        systemContext email_system "Context" {
            include *
            autolayout lr
        }

        // C2
        container email_system "Containers" {
            include *
            autolayout lr
        }

        // C3 
        component api_server "ComponentsAPI" {
            include *
            autolayout lr
        }
        // C4
        dynamic email_system "CreateMessage" {
            user -> web_app "Создает письмо через интерфейс"
            web_app -> api_server "Передает запрос на создание нового письма"
            api_server -> database "Сохраняет данные о новом письме"
            database -> api_server "Возвращает подтверждение сохранения письма"
            api_server -> web_app "Создает ответ на запрос о создании письма"
            web_app -> user "Оповещает об удачном/неудачном создании письма"
        }
    }
}
