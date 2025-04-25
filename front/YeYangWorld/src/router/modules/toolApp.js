import ToolBegin from '/src/view/toolApp/ToolBegin.vue';
import Crawl from '/src/view/toolApp/Crawl.vue';
import Markdown from '/src/view/toolApp/Markdown.vue';

export default [
    {
        path : '/toolbegin',
        component : ToolBegin,
    },
    {
        path : '/toolbegin/crawl',
        component : Crawl,
    },
    { 
        path : '/toolbegin/markdown',
        component : Markdown,
    }
]