<div>

    <h3>Recent Posts</h3>

    <ul>

    % for entry in recent:
        <li>
            <a href="/post/{{ entry['id'] }}">{{ entry['name'] }}</a>
        </li>
    % end
    

    </ul>
    <a href="/posts">View all posts</a>

</div>
