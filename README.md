# Lingvanex-test-task
Доброго времени суток. Вот актуальный результат моей работы.

В данном скрипте процесс парсинга происходит построчно, для того, чтобы не занимать много места в оперативной памяти.
Исходя из поставленной задачи и указанного формата, разбил каждую строку (по табуляции) на английский вариант
и его актуальный перевод. 

Далее производится проверка на количество вариантов перевода.

Если одному английскому слову соответствует одно русское слово - не заходим в циклы и сразу добавляем в файлы слова.

Если же существует более одного варианта перевода, то каждое английское слово добавляется в файл ТАКОЕ количество раз,
которому соответствует количество переводов этого слова.

И в случае если есть несколько английских вариантов, то русский перевод пишется столько раз, сколько имеется вариантов английского.


Надеюсь, что понятно описал логику выполнения данной задачи :)
