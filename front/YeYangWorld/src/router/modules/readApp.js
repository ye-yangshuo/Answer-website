import ReadBegin from '/src/view/readApp/ReadBegin.vue'
import EnglishArticle from '/src/view/readApp/EnglishArticle.vue'
import EnglishBook from '/src/view/readApp/EnglishBook.vue'
import ChineseArticle from '/src/view/readApp/ChineseArticle.vue'
import ChineseBook from '/src/view/readApp/ChineseBook.vue'
export default[
    {
        path: '/readbegin',
        name: 'readbegin',
        component: ReadBegin,
        children: [
            {
                path: '/readbegin/englisharticle',
                name: 'englisharticle',
                component: EnglishArticle
            },
            {
                path: '/readbegin/englishbook',
                name: 'englishbook',
                component: EnglishBook
            },
            {
                path: '/readbegin/chinesearticle',
                name: 'chinesearticle',
                component: ChineseArticle
            },
            {
                path: '/readbegin/chinesebook',
                name: 'chinesebook',
                component: ChineseBook
            }
        ]

    },


];