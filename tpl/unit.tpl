<div>

    <h3>Lessons about "{{ unit['name'] }}"</h3>

    <ul>

    % for lesson in lessons:
        <li>
            <a href="/lesson/{{ lesson['id'] }}">{{ lesson['name'] }}</a>
        </li>
    % end

    </ul>

</div>

<br/>

<a href="/">Go home</a>
