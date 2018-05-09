(function () {

    var bv = new Bideo();
    bv.init({
        // Video element
        videoEl: document.querySelector('#background_video'),

        // Container element
        container: document.querySelector('body'),

        // Resize
        resize: true,

        // autoplay: false,

        isMobile: window.matchMedia('(max-width: 768px)').matches,

        playButton: document.querySelector('#play'),
        pauseButton: document.querySelector('#pause'),

        // Array of objects containing the src and type
        // of different video formats to add
        src: [
            {
                //晚霞
                src:'http://video.699pic.com/videos/69/30/47/yDWM0f7cNbU71520693047.mp4',
                //自然环境
                //src:'http://video.699pic.com/videos/95/31/93/bicHjjJtg5Es1521953193.mp4',
                // src:'http://video.699pic.com/videos/28/24/87/IPTjyXf0kZKK1525282487.mp4',
                //src:'http://cdn.tubangzhu.com/static/tbz-main/images/v4/bg2.mp4',
                //src: 'https://media.html5media.info/video.mp4',
                //src:'http://video.699pic.com/videos/96/61/18/315gJeUfrsIg1524966118.mp4',
                //cloud.video.taobao.com/play/u/3245834217/p/1/e/6/t/1/50021244141.mp4
                //src: 'http://ak4.picdn.net/shutterstock/videos/4170274/preview/stock-footage-beautiful-girl-lying-on-the-meadow-and-dreaming-enjoy-nature-close-up-slow-motion-footage.mp4',
                type: 'video/mp4'
            },
            {
                src: 'night.webm',
                type: 'video/webm;codecs="vp8, vorbis"'
            }
        ],

        // What to do once video loads (initial frame)
        onLoad: function () {
            document.querySelector('#video_cover').style.display = 'none';
        }
    });
}());
