% rebase('/data/app/web/tpl/base.tpl')
<h3>All posts:</h3>
% for entry in posts:
        <div class="entry-title">
        <div class="entry-text">
            <a href="/post/{{entry['id']}}">{{entry['name']}}</a><br>
            <span class="entry-date">{{entry['created']}}</span>
        </div><br>
        </div>
% end
