package com.teamtreehouse.courses.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by zerom_000 on 7/8/2016.
 * added implements CourseIdeaDAO
 * then it complained and we generated the methods
 */
public class SimpleCourseIdeaDAO implements CourseIdeaDAO {
    private List<CourseIdea> ideas;

    public SimpleCourseIdeaDAO() {
        ideas = new ArrayList<>();
    }

    @Override
    public boolean add(CourseIdea idea) {
        return ideas.add(idea);
    }

    @Override
    public List<CourseIdea> findAll() {
        return new ArrayList<>(ideas);
    }

    @Override
    public CourseIdea findBySlug(String slug) {
        return ideas.stream().filter(idea -> idea.getSlug().equals(slug)).findFirst().orElseThrow(NotFoundException::new);
    }
}
