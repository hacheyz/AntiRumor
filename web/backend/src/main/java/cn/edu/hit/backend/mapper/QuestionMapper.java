package cn.edu.hit.backend.mapper;

import cn.edu.hit.backend.pojo.Question;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.time.LocalDate;
import java.util.List;

@Mapper
public interface QuestionMapper {

  @Insert("insert into question(question, create_date, num_agree, num_disagree, expert_conclusion) " +
      "values(#{question}, #{create_date}, 0, 0, '')")
  public void add(String question, LocalDate create_date);

  List<Question> pagelist(@Param("searchQuestion") String searchQuestion);
}