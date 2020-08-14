const axios = require('axios').default;

axios.get('https://gist.githubusercontent.com/ferasbg/1505d133182544f26ff50e684a7ea050/raw/4beda07392d4607f63bd96e6ab1a5f7115ebd83b/core.json').then(function (response) {
    console.log(response)
})
